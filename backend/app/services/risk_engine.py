import os
import joblib
import numpy as np

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "..", "ai-model", "models", "subsidence_model.joblib")

class SubsidenceRiskEngine:
    def __init__(self):
        self.model_data = None
        self.load_model()

    def load_model(self):
        if os.path.exists(MODEL_PATH):
            try:
                self.model_data = joblib.load(MODEL_PATH)
                print("Successfully loaded trained ML Subsidence Model.")
            except Exception as e:
                print(f"Could not load ML model: {e}. Using geotechnical formula engine.")
        else:
            print("ML model joblib file not found yet. Using physics-based formula engine.")

    def predict_risk(self, tilt: float, displacement: float, crack_width: float, 
                     vibration: float, load_change: float, rate_tilt: float = 0.0, 
                     rate_disp: float = 0.0, rate_crack: float = 0.0) -> dict:
        """
        Calculates risk_score (0-100) and risk_level (LOW, MEDIUM, HIGH, CRITICAL).
        """
        if self.model_data:
            try:
                features = np.array([[
                    tilt, displacement, crack_width, vibration,
                    load_change, 28.0, 80.0, rate_tilt, rate_disp, rate_crack
                ]])
                scaled = self.model_data['scaler'].transform(features)
                score = float(self.model_data['regressor'].predict(scaled)[0])
                score = float(np.clip(score, 0.0, 100.0))
            except Exception:
                score = self._formula_risk(tilt, displacement, crack_width, vibration, load_change, rate_tilt, rate_disp)
        else:
            score = self._formula_risk(tilt, displacement, crack_width, vibration, load_change, rate_tilt, rate_disp)

        # Classification
        if score < 25.0:
            level = "LOW"
        elif score < 50.0:
            level = "MEDIUM"
        elif score < 75.0:
            level = "HIGH"
        else:
            level = "CRITICAL"

        # Contributing factor breakdown
        factors = []
        if tilt > 3.0:
            factors.append({"factor": "Roof Tilt Angle (°)", "impact": "Critical", "weight": "35%"})
        if displacement > 8.0:
            factors.append({"factor": "Roof Strata Displacement", "impact": "High", "weight": "30%"})
        if crack_width > 3.0:
            factors.append({"factor": "Crack Width Opening", "impact": "High", "weight": "20%"})
        if vibration > 0.5:
            factors.append({"factor": "Ground Vibration Peak", "impact": "Moderate", "weight": "15%"})

        if not factors:
            factors.append({"factor": "Baseline Telemetry", "impact": "Low", "weight": "100%"})

        return {
            "risk_score": round(score, 1),
            "risk_level": level,
            "primary_factor": factors[0]["factor"],
            "contributing_factors": factors,
            "confidence": 0.95
        }

    def _formula_risk(self, tilt, displacement, crack_width, vibration, load_change, rate_tilt, rate_disp):
        raw = (
            tilt * 3.5 +
            displacement * 1.8 +
            crack_width * 3.0 +
            vibration * 15.0 +
            load_change * 0.3 +
            rate_tilt * 12.0 +
            rate_disp * 8.0
        )
        return float(np.clip(raw, 0.0, 100.0))

risk_engine = SubsidenceRiskEngine()
