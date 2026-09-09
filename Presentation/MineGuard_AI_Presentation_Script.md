# 🎤 SIH 2026 Internal Hackathon Pitching Script & Slide Breakdown
**Project:** MineGuard AI | **Problem Statement ID:** SIH26025  
**Team Name:** MineNova6 | **Presentation File:** `MineGuard_AI_SIH2026_Internal_Presentation.pptx`

---

## 📋 SLIDE-BY-SLIDE CONTENT & SPEAKER SCRIPT

### SLIDE 1: Title Slide (Dark Theme Hero)
- **Visual Layout:** Premium dark slate card with cyan title badge, bold project name "MineGuard AI", subtitle, and team credits.
- **Speaker (Monika):**  
  > *"Respected Judges, good morning. We are Team MineNova6, and today we are presenting **MineGuard AI** — an AI-enabled, low-cost, real-time mine subsidence monitoring, prediction, and early warning system for underground coal mines in India, addressing Problem Statement **SIH26025**."*

---

### SLIDE 2: The Underground Coal Mining Subsidence Challenge
- **Visual Layout:** 3 high-impact cards outlining fatalities, high cabling costs (>₹5 Lakhs/panel), and zero pre-collapse warning.
- **Speaker (Monika):**  
  > *"In Indian coalfields like Jharia and Raniganj, roof falls and mine subsidence cause over **40% of underground mining fatalities**. Traditional cabled monitoring systems are extremely expensive, costing over ₹5 Lakhs per panel, and their cables frequently snap during rock movement—disabling safety systems exactly when needed. Current solutions rely on static thresholds that trigger too late, leaving miners zero evacuation time before catastrophic roof collapse."*

---

### SLIDE 3: Proposed Solution — MineGuard AI Ecosystem
- **Visual Layout:** 4 grid cards highlighting Wireless ESP32 LoRa Mesh (₹1,590/node), AI Subsidence Predictor, Command Center Dashboard, and Dual Alarm Sirens.
- **Speaker (Monika):**  
  > *"MineGuard AI solves this with a 4-layer ecosystem:  
  > First, ultra-low-cost ₹1,590 wireless ESP32 LoRa nodes operating at 868MHz that penetrate rock strata without expensive cabling.  
  > Second, an AI Subsidence Predictor using Random Forest ML that correlates 10 parameters—placing 42% weight on 5-minute displacement velocity ($\Delta disp/\Delta t$) to detect pre-failure roof sagging in Stage 1.  
  > Third, a web command center dashboard with an interactive Leaflet underground seam map.  
  > And fourth, dual fail-safe alarm sirens—local 1kHz ESP32 buzzers plus real-time dashboard notifications."*

---

### SLIDE 4: End-to-End System Architecture & Data Flow
- **Visual Layout:** 7-step horizontal pipeline from Sensors to Command Center, highlighting FastAPI Backend & AI Risk Engine.
- **Speaker (Shareque):**  
  > *"Here is our end-to-end data pipeline:  
  > Multi-sensor telemetry (MPU6050 tilt, string pot displacement, load cell stress) is sampled by the ESP32 node and broadcast over 868MHz LoRa. The gateway hub receives the packet and posts JSON data to our Python FastAPI REST backend. The backend passes telemetry through our trained Random Forest ML engine, calculates a 0–100 risk score, logs records to SQLite, and updates the React dashboard in real time."*

---

### SLIDE 5: Technical Innovation & Live SIH Demonstration
- **Visual Layout:** 4 feature cards detailing velocity weighting, SIH Emergency Simulator, cross-device sync, and DGMS compliance.
- **Speaker (Shareque — *Triggers SIH Demo Bar on Screen*):**  
  > *"Our key innovation is **velocity weighting**—predicting rock failure before static threshold breaches.  
  > As you see on screen, we built an interactive **SIH Emergency Simulator**. When I click 'Subsidence Event', Node N5's risk score instantly spikes to 82 CRITICAL, its marker on the Leaflet map highlights with a pulsing red danger ring, and an early warning alert is logged automatically.  
  > Furthermore, our telemetry engine uses global Epoch time seeding and `BroadcastChannel` sync, so judges can open our live Vercel URL on their phones and see identical real-time data."*

---

### SLIDE 6: Feasibility, Low-Cost Analysis & Scalability
- **Visual Layout:** Left side: Component BOM table (~₹1,590/node). Right side: Commercial advantages (96% cost reduction, PostgreSQL/TimescaleDB scaling, Vercel cloud hosting).
- **Speaker (Monika):**  
  > *"In terms of feasibility, imported commercial wired sensors cost ₹50,000+ per unit. MineGuard AI delivers a complete multi-sensor wireless node for just **₹1,590 ($19 USD)**—a 96% cost reduction.  
  > Architecturally, our SQLAlchemy database layer is decoupled, allowing instant scaling to PostgreSQL with TimescaleDB time-series indexing for 100+ mine nodes. The frontend is live on Vercel for instant access by control room engineers."*

---

### SLIDE 7: Team MineNova6 & Conclusion
- **Visual Layout:** 6 team member cards with defined responsibilities and green closing banner.
- **Speaker (Monika & Shareque):**  
  > *"MineGuard AI was built collaboratively by Team MineNova6:  
  > Shareque on System Architecture, Monika on Geotechnical Research, Aditya on UI/UX, Farhan on Frontend React, Atharva on Backend FastAPI, and Affan on AI/ML.  
  > We are fully prepared for field testing in active coal seams to protect underground miners across India. Thank you!"*

---

## 🎯 PITCHING TIPS FOR INTERNAL HACKATHON

1. **Keep it under 6 minutes:** Slide 1-3 (2 mins), Slide 4-5 Live Demo (2.5 mins), Slide 6-7 (1.5 mins).
2. **Show the Live Vercel Dashboard:** During Slide 5, Shareque should switch to the live browser tab and click the **Subsidence Event** demo button live on stage to impress the judges!
3. **Bring the ESP32 Hardware (if assembled):** Hold up the ESP32 + MPU6050 board when Monika speaks on Slide 3.
