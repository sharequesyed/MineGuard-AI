# MineGuard AI — Hardware Assembly & Integration Guide
**Team:** MineNova6 | **Problem Statement ID:** SIH26025

---

## 1. Bill of Materials (BOM) & Low-Cost Hardware Budget

| Component | Function | Approx. Cost (INR) |
| :--- | :--- | :--- |
| **ESP32 Node (Microcontroller)** | Core processing, ADC sensor reading, LoRa transmitter | ₹450 |
| **SX1276 LoRa Module (868 MHz)** | Long-range wireless radio communication through rock strata | ₹350 |
| **MPU6050 6-Axis Gyro/Accelerometer** | Detects roof tilt angle & ground vibration acceleration | ₹180 |
| **Linear Potentiometer / String Pot** | Simulates roof strata displacement & crack width growth | ₹80 |
| **HX711 + 5kg Load Cell** | Measures pillar & roof support load stress changes | ₹180 |
| **DHT22 Sensor** | Ambient temperature & humidity monitoring | ₹160 |
| **3.7V 18650 LiFePO4 Battery + TP4056** | Rechargeable power supply with solar/battery charging | ₹150 |
| **5V Active Buzzer + Red LED** | Local audible/visual warning sirens | ₹40 |
| **Total Hardware Cost per Node:** | **~ ₹1,590 ($19 USD)** — Extremely Low-Cost |

---

## 2. Wiring & Pinout Schematic (ESP32 Sensor Node)

### A. MPU6050 Tilt Sensor (I2C)
- `VCC` → ESP32 `3.3V`
- `GND` → ESP32 `GND`
- `SDA` → ESP32 `GPIO 21`
- `SCL` → ESP32 `GPIO 22`

### B. SX1276 LoRa Radio Module (SPI)
- `VCC` → ESP32 `3.3V`
- `GND` → ESP32 `GND`
- `SCK` → ESP32 `GPIO 18`
- `MISO` → ESP32 `GPIO 19`
- `MOSI` → ESP32 `GPIO 23`
- `NSS (SS)` → ESP32 `GPIO 5`
- `RST` → ESP32 `GPIO 14`
- `DIO0` → ESP32 `GPIO 2`

### C. Analog Displacement & Crack Potentiometers (ADC)
- Potentiometer 1 (Displacement): Pin `Signal` → ESP32 `GPIO 34` (ADC1_CH6)
- Potentiometer 2 (Crack Width): Pin `Signal` → ESP32 `GPIO 35` (ADC1_CH7)
- VCC → `3.3V`, GND → `GND`

### D. Warning Sirens
- Red Emergency LED: Anode (+) → ESP32 `GPIO 12` (via 220Ω resistor)
- Active 5V Buzzer: Positive (+) → ESP32 `GPIO 13`

---

## 3. Step-by-Step Hardware Assembly

1. **Breadboard / PCB Setup:** Place ESP32 on a breadboard or solder onto a perfboard.
2. **Wire MPU6050:** Connect SDA (GPIO 21) and SCL (GPIO 22) to enable 6-axis tilt and vibration tracking.
3. **Connect LoRa Transceiver:** Wire SPI pins (GPIO 18, 19, 23, 5, 14, 2) and attach the 868MHz spring/whip antenna.
4. **Attach Potentiometers:** Connect slider potentiometers to simulate physical displacement (0–50mm) and crack width (0–20mm).
5. **Connect Power:** Wire the 18650 LiFePO4 battery through the TP4056 charging module to ESP32 `5V` or `3.3V` pin.

---

## 4. How to Connect Physical Hardware to Software Backend

```
[ Physical ESP32 Sensor Node (N5) ]
         │
         │  (Transmits 868MHz LoRa Packets: "N5,4.82,14.50,5.10,0.825,29.4,96.5")
         ▼
[ Physical ESP32 LoRa Gateway (Receiver Hub) ]
         │
         │  (Option A: Wi-Fi HTTP POST to http://192.168.1.10:8000/api/sensors/data)
         │  (Option B: USB Serial Cable to Laptop running Python Serial Bridge)
         ▼
[ FastAPI Backend (Python) ]
         │
         │  (Evaluates AI Model & Risk Score: 82 CRITICAL)
         ▼
[ React Web Dashboard (Live Browser) ]
```

### Option A: Direct Wi-Fi Connection (ESP32 Gateway -> FastAPI Backend)
1. Open `hardware/esp32/mineguard_gateway.ino` in Arduino IDE.
2. Change `WIFI_SSID` and `WIFI_PASS` to your Wi-Fi router / mobile hotspot name and password.
3. Change `BACKEND_URL` to `http://<YOUR_LAPTOP_IP>:8000/api/sensors/data`.
4. Upload code to the Gateway ESP32. When a node transmits, the gateway automatically posts the data into the backend!

### Option B: USB Cable Connection (Serial Bridge - No Wi-Fi Needed)
If Wi-Fi is unavailable in the competition venue:
1. Connect Gateway ESP32 to laptop via USB cable.
2. Run the provided Python serial bridge:
   ```bash
   python hardware/sensor_simulator/serial_bridge.py --port COM3
   ```
3. The bridge reads incoming USB serial bytes and forwards them directly to `http://localhost:8000/api/sensors/data`.
