# MineGuard AI — LoRa Telemetry Payload Specification
**Team:** MineNova6  
**Problem Statement ID:** SIH26025

---

## 1. Frequency Band & Modulation
- **Carrier Frequency:** 868.0 MHz (License-free ISM Band in India)
- **Modulation:** LoRa Chirp Spread Spectrum (CSS)
- **Bandwidth:** 125 kHz
- **Spreading Factor (SF):** SF7 (fast transmission, low latency)
- **Coding Rate:** 4/5

---

## 2. ASCII CSV Payload Packet Format (Simplicated)
ESP32 nodes transmit lightweight CSV payload strings:
`NODE_ID,TILT_DEG,DISP_MM,CRACK_MM,VIB_G,TEMP_C,BAT_PCT`

### Example Packet:
`N5,4.82,14.50,5.10,0.825,29.4,96.5`

### Field Breakdown:
| Byte / Field | Variable Name | Type | Description |
| :--- | :--- | :--- | :--- |
| `[0..1]` | `NODE_ID` | String | Node identifier (`N1` to `N6`) |
| `[2]` | `TILT_DEG` | Float | MPU6050 tilt angle displacement (°) |
| `[3]` | `DISP_MM` | Float | Roof displacement potentiometer (mm) |
| `[4]` | `CRACK_MM` | Float | Surface crack growth sensor (mm) |
| `[5]` | `VIB_G` | Float | Ground peak vibration acceleration (g) |
| `[6]` | `TEMP_C` | Float | MPU6050 ambient temperature (°C) |
| `[7]` | `BAT_PCT` | Float | LiFePO4 battery percentage (%) |
