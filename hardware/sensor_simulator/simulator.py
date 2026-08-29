import time
import random
import requests

API_URL = "http://localhost:8000/api/sensors/data"

NODES = ["N1", "N2", "N3", "N4", "N5", "N6"]

def run_sensor_simulation(interval=3.0):
    print("Starting MineGuard AI Sensor Telemetry Simulator...")
    print(f"Targeting API endpoint: {API_URL}")
    print("Simulating 6 LoRa sensor nodes (N1 to N6) with progressive deformation physics...\n")

    # Initial baseline values
    state = {
        node: {
            "tilt": random.uniform(0.2, 0.8),
            "displacement": random.uniform(0.5, 1.5),
            "crack_width": random.uniform(0.0, 0.3),
            "vibration": random.uniform(0.02, 0.08),
            "load_change": random.uniform(1.0, 4.0),
            "temperature": round(random.uniform(26.0, 30.0), 1),
            "humidity": round(random.uniform(75.0, 85.0), 1),
            "battery": round(random.uniform(90.0, 100.0), 1)
        }
        for node in NODES
    }

    step = 0
    while True:
        step += 1
        print(f"--- Telemetry Broadcast Tick #{step} ---")

        for node_id in NODES:
            n = state[node_id]

            # Simulate slight organic drift
            n["tilt"] = max(0.1, round(n["tilt"] + random.uniform(-0.02, 0.03), 2))
            n["displacement"] = max(0.2, round(n["displacement"] + random.uniform(-0.05, 0.08), 2))
            n["crack_width"] = max(0.0, round(n["crack_width"] + random.uniform(-0.01, 0.02), 2))
            n["vibration"] = max(0.01, round(n["vibration"] + random.uniform(-0.005, 0.01), 3))
            n["load_change"] = round(n["load_change"] + random.uniform(-0.2, 0.4), 1)

            payload = {
                "node_id": node_id,
                "tilt": n["tilt"],
                "displacement": n["displacement"],
                "crack_width": n["crack_width"],
                "vibration": n["vibration"],
                "load_change": n["load_change"],
                "temperature": n["temperature"],
                "humidity": n["humidity"],
                "battery": n["battery"]
            }

            try:
                res = requests.post(API_URL, json=payload, timeout=2.0)
                if res.status_code == 200:
                    data = res.json()
                    print(f" [{node_id}] Sent Telemetry -> ID: {data.get('id')} | Tilt: {n['tilt']}° | Disp: {n['displacement']}mm")
                else:
                    print(f" [{node_id}] HTTP Error {res.status_code}")
            except Exception as e:
                print(f" [{node_id}] Local simulation active (Backend offline or starting up)")

        time.sleep(interval)

if __name__ == '__main__':
    run_sensor_simulation()
