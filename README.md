# MineGuard AI — Real-Time Mine Subsidence Monitoring & Early Warning System

**Team Name:** MineNova6  
**Problem Statement ID:** SIH26025  
**Hackathon:** Smart India Hackathon (SIH) 2026  
**Problem Statement:** Development of an AI-enabled Low Cost Real Time Mine Subsidence Monitoring, Prediction and Early Warning System for Underground Coal Mines in India.

---

## 🌟 Overview
MineGuard AI is a functional, low-cost engineering MVP designed to protect underground coal miners in India. It monitors roof strata tilt, displacement, crack growth, vibration acceleration, and load stress in real time using ESP32 LoRa wireless sensor nodes, predicts mine subsidence risk using a Random Forest machine learning pipeline, isolates high-risk underground seams, and triggers instant early warning sirens.

---

## 🚀 Tech Stack

### Frontend
- **Framework:** React + Vite
- **Styling:** Tailwind CSS (Light Theme default with Dark Mode toggle)
- **Design:** Glassmorphism UI, subtle Dot Matrix canvas background
- **Visualization:** Recharts (telemetry line graphs), Leaflet / OpenStreetMap (underground seam map)
- **Deployment:** Vercel

### Backend
- **Framework:** Python FastAPI
- **Database:** SQLite / SQLAlchemy (PostgreSQL / TimescaleDB ready)
- **Architecture:** REST API + WebSocket real-time broadcast engine

### AI / Machine Learning
- **Libraries:** scikit-learn, pandas, NumPy, joblib
- **Model:** Random Forest Regressor & Classifier evaluating 10 telemetric parameters including 5-minute velocity rates of change ($\Delta tilt / \Delta t$, $\Delta disp / \Delta t$)
- **Performance:** Mean Absolute Error (MAE): 1.27 | $R^2$: 0.9969

### Hardware & LoRa
- **Microcontroller:** ESP32 (32-bit dual-core MCU)
- **Radio:** SX1276 LoRa 868MHz (Long-range telemetry through rock strata)
- **Sensors:** MPU6050 (6-axis gyro/accel), String Potentiometers (displacement & crack width), Load Cell + HX711, DHT22
- **Cost:** ~ ₹1,590 ($19 USD) per sensor node (Extremely low cost)

---

## 👥 Team MineNova6
- **Shareque:** Team Leader + Tech Lead + System Integration
- **Monika:** Presentation + Documentation + Geotechnical Research
- **Aditya:** UI/UX Design Lead
- **Farhan:** Frontend React Engineer
- **Atharva:** Backend FastAPI Lead
- **Affan:** AI/ML & Data Lead

---

## ⚡ Quickstart Guide

### 1. Frontend
```bash
cd frontend
npm install
npm run dev
```

### 2. Backend
```bash
cd backend
pip install -r requirements.txt
python run.py
```

### 3. Sensor Node Telemetry Simulator
```bash
python hardware/sensor_simulator/simulator.py
```
