import os
import numpy as np
import pandas as pd

def generate_synthetic_mine_data(num_samples=5000, random_state=42):
    """
    Generates a realistic synthetic dataset for underground coal mine subsidence risk prediction.
    Features model geotechnical correlations between tilt, displacement, crack width, vibration, load change,
    and rate of change indicators.
    """
    np.random.seed(random_state)
    
    # 1. Normal state (60%), Warning state (25%), Subsidence state (15%)
    states = np.random.choice(['NORMAL', 'WARNING', 'SUBSIDENCE'], size=num_samples, p=[0.60, 0.25, 0.15])
    
    nodes = [f"N{i}" for i in range(1, 7)]
    node_ids = np.random.choice(nodes, size=num_samples)
    
    tilt = []
    displacement = []
    crack_width = []
    vibration = []
    load_change = []
    temperature = []
    humidity = []
    battery = []
    
    rate_tilt = []
    rate_disp = []
    rate_crack = []
    
    for state in states:
        if state == 'NORMAL':
            # Stable underground conditions
            t = np.random.uniform(0.1, 1.2)
            d = np.random.uniform(0.2, 2.5)
            c = np.random.uniform(0.0, 1.0)
            v = np.random.uniform(0.02, 0.18)
            l = np.random.uniform(-2.0, 5.0)
            rt = np.random.uniform(0.0, 0.05)
            rd = np.random.uniform(0.0, 0.1)
            rc = np.random.uniform(0.0, 0.02)
        elif state == 'WARNING':
            # Accelerated movement / strata instability
            t = np.random.uniform(1.2, 3.5)
            d = np.random.uniform(2.5, 8.0)
            c = np.random.uniform(1.0, 4.0)
            v = np.random.uniform(0.18, 0.75)
            l = np.random.uniform(5.0, 35.0)
            rt = np.random.uniform(0.05, 0.3)
            rd = np.random.uniform(0.1, 0.8)
            rc = np.random.uniform(0.02, 0.25)
        else: # SUBSIDENCE / HAZARD
            # Severe deformation & active collapse risk
            t = np.random.uniform(3.5, 12.0)
            d = np.random.uniform(8.0, 45.0)
            c = np.random.uniform(4.0, 22.0)
            v = np.random.uniform(0.75, 4.2)
            l = np.random.uniform(35.0, 110.0)
            rt = np.random.uniform(0.3, 1.8)
            rd = np.random.uniform(0.8, 4.5)
            rc = np.random.uniform(0.25, 1.5)
            
        temp = np.random.uniform(24.0, 38.0) + (1.5 if state == 'SUBSIDENCE' else 0.0)
        hum = np.random.uniform(65.0, 95.0)
        bat = np.random.uniform(60.0, 100.0)
        
        tilt.append(round(t, 2))
        displacement.append(round(d, 2))
        crack_width.append(round(c, 2))
        vibration.append(round(v, 3))
        load_change.append(round(l, 2))
        temperature.append(round(temp, 1))
        humidity.append(round(hum, 1))
        battery.append(round(bat, 1))
        
        rate_tilt.append(round(rt, 3))
        rate_disp.append(round(rd, 3))
        rate_crack.append(round(rc, 3))
        
    df = pd.DataFrame({
        'node_id': node_ids,
        'state': states,
        'tilt': tilt,
        'displacement': displacement,
        'crack_width': crack_width,
        'vibration': vibration,
        'load_change': load_change,
        'temperature': temperature,
        'humidity': humidity,
        'battery': battery,
        'rate_tilt_5m': rate_tilt,
        'rate_disp_5m': rate_disp,
        'rate_crack_5m': rate_crack
    })
    
    # Calculate ground truth risk score (0-100) using geotechnical weighting
    raw_score = (
        df['tilt'] * 3.2 +
        df['displacement'] * 1.6 +
        df['crack_width'] * 2.8 +
        df['vibration'] * 14.0 +
        df['load_change'] * 0.35 +
        df['rate_tilt_5m'] * 12.0 +
        df['rate_disp_5m'] * 8.0 +
        df['rate_crack_5m'] * 10.0 +
        np.random.normal(0, 1.5, size=num_samples)
    )
    
    # Clip risk score between 0 and 100
    df['risk_score'] = np.clip(np.round(raw_score, 1), 0.0, 100.0)
    
    # Categorize risk level according to SIH prompt thresholds
    # 0-25: LOW, 25-50: MEDIUM, 50-75: HIGH, 75-100: CRITICAL
    conditions = [
        (df['risk_score'] < 25.0),
        (df['risk_score'] >= 25.0) & (df['risk_score'] < 50.0),
        (df['risk_score'] >= 50.0) & (df['risk_score'] < 75.0),
        (df['risk_score'] >= 75.0)
    ]
    choices = ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL']
    df['risk_level'] = np.select(conditions, choices, default='LOW')
    
    return df

if __name__ == '__main__':
    out_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)
    csv_path = os.path.join(out_dir, 'synthetic_mine_subsidence_dataset.csv')
    df = generate_synthetic_mine_data(num_samples=6000)
    df.to_csv(csv_path, index=False)
    print(f"Generated synthetic mine subsidence dataset with {len(df)} samples at: {csv_path}")
    print(df['risk_level'].value_counts())
