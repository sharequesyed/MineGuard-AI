import argparse
import json
import requests

try:
    import serial
except ImportError:
    print("pyserial package not installed yet. Install via: pip install pyserial")

API_URL = "http://localhost:8000/api/sensors/data"

def listen_serial_and_forward(port="COM3", baud=115200):
    print(f"Connecting to ESP32 Gateway via Serial Port: {port} @ {baud} baud...")
    try:
        ser = serial.Serial(port, baud, timeout=1)
        print("Connected! Listening for live hardware LoRa packets...\n")
        
        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line.startswith("FORWARD_SERIAL:"):
                json_str = line.replace("FORWARD_SERIAL:", "")
                try:
                    payload = json.loads(json_str)
                    res = requests.post(API_URL, json=payload, timeout=2.0)
                    print(f"Hardware Telemetry Ingested ({payload.get('node_id')}) -> Status: {res.status_code}")
                except Exception as e:
                    print(f"Error posting serial telemetry: {e}")
    except Exception as e:
        print(f"Serial port connection error on {port}: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="MineGuard AI USB Serial Bridge")
    parser.add_argument("--port", default="COM3", help="Serial port (e.g. COM3 on Windows or /dev/ttyUSB0 on Linux)")
    args = parser.parse_args()
    listen_serial_and_forward(port=args.port)
