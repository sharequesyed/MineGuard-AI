import os
import sys
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score, classification_report

def train_subsidence_model():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(current_dir, '..', 'dataset', 'synthetic_mine_subsidence_dataset.csv')
    
    if not os.path.exists(dataset_path):
        print("Dataset not found. Generating synthetic dataset first...")
        sys.path.append(os.path.join(current_dir, '..', 'dataset'))
        from generate_dataset import generate_synthetic_mine_data
        df = generate_synthetic_mine_data(num_samples=6000)
        os.makedirs(os.path.dirname(dataset_path), exist_ok=True)
        df.to_csv(dataset_path, index=False)
    else:
        df = pd.read_csv(dataset_path)
        
    feature_cols = [
        'tilt', 'displacement', 'crack_width', 'vibration',
        'load_change', 'temperature', 'humidity',
        'rate_tilt_5m', 'rate_disp_5m', 'rate_crack_5m'
    ]
    
    X = df[feature_cols]
    y_score = df['risk_score']
    y_level = df['risk_level']
    
    X_train, X_test, y_score_train, y_score_test, y_level_train, y_level_test = train_test_split(
        X, y_score, y_level, test_size=0.2, random_state=42
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train Random Forest Regressor for continuous Risk Score (0-100)
    regressor = RandomForestRegressor(n_estimators=100, max_depth=12, random_state=42)
    regressor.fit(X_train_scaled, y_score_train)
    
    # Train Classifier for Risk Level
    classifier = RandomForestClassifier(n_estimators=100, max_depth=12, random_state=42)
    classifier.fit(X_train_scaled, y_level_train)
    
    # Evaluate
    score_preds = regressor.predict(X_test_scaled)
    level_preds = classifier.predict(X_test_scaled)
    
    mae = mean_absolute_error(y_score_test, score_preds)
    r2 = r2_score(y_score_test, score_preds)
    
    print(f"Model Training Results:")
    print(f" - Risk Score MAE: {mae:.2f}")
    print(f" - Risk Score R2: {r2:.4f}")
    print("\nClassification Report for Risk Level:")
    print(classification_report(y_level_test, level_preds))
    
    # Feature Importance Breakdown
    importances = regressor.feature_importances_
    importance_df = pd.DataFrame({
        'feature': feature_cols,
        'importance': importances
    }).sort_values(by='importance', ascending=False)
    print("\nTop Contributing Factors (Feature Importances):")
    print(importance_df.to_string(index=False))
    
    # Save Model Bundle
    models_dir = os.path.join(current_dir, '..', 'models')
    os.makedirs(models_dir, exist_ok=True)
    model_bundle_path = os.path.join(models_dir, 'subsidence_model.joblib')
    
    joblib.dump({
        'regressor': regressor,
        'classifier': classifier,
        'scaler': scaler,
        'feature_cols': feature_cols,
        'metrics': {'mae': mae, 'r2': r2},
        'feature_importances': importance_df.to_dict(orient='records')
    }, model_bundle_path)
    
    print(f"\nTrained model bundle successfully saved to: {model_bundle_path}")

if __name__ == '__main__':
    train_subsidence_model()
