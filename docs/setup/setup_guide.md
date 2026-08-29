# MineGuard AI — Local Setup & Quickstart Guide
**Team:** MineNova6 | **Problem Statement ID:** SIH26025

---

## 1. Prerequisites
- **Node.js:** v18.0.0 or higher
- **Python:** v3.10 or higher

---

## 2. Running the Frontend Dashboard (React + Vite)
```bash
cd frontend
npm install
npm run dev
```
The React monitoring dashboard will open at `http://localhost:5173`.

---

## 3. Running the FastAPI Backend Server
```bash
cd backend
pip install -r requirements.txt
python app/main.py
```
The REST API server will run at `http://localhost:8000`.  
Swagger Interactive API documentation is available at `http://localhost:8000/docs`.

---

## 4. Training the AI Subsidence Model
```bash
python ai-model/training/train_model.py
```
This script generates the synthetic geotechnical dataset and trains the Random Forest classifier and regressor, saving the model bundle to `ai-model/models/subsidence_model.joblib`.

---

## 5. Launching the Sensor Node Simulator
```bash
python hardware/sensor_simulator/simulator.py
```
Simulates continuous telemetric data transmission from 6 underground LoRa nodes (N1 to N6) to the FastAPI backend.
