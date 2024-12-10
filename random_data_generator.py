import random
import time
import requests
from datetime import datetime

SERVER_URL = "http://127.0.0.1:5000/traffic"  # Update to your server if needed

def generate_random_traffic_data():
    junctions = 20
    devices_per_junction = 4  # 4 devices assume per junction

    while True:
        for junction_id in range(1, junctions + 1):
            payloads = []  # To store payloads for each device
            for device_id in range(1, devices_per_junction + 1):
                vehicle_count = random.randint(0, 50)  # Generate random vehicle count
                air_quality = random.uniform(0, 100)  # Generate random air quality
                payload = {
                    'junction_id': junction_id,
                    'device_id': f'Device_{(junction_id-1)*devices_per_junction + device_id}',
                    'vehicle_count': vehicle_count,
                    'air_quality': air_quality,
                    'timestamp': datetime.now().isoformat()
                }
                payloads.append(payload)

                # Send data to server
                response = requests.post(SERVER_URL, json=payload)
                if response.status_code == 200:
                    signal_response = response.json()
                    print(f"Junction: {signal_response['junction_id']}, Signals: {signal_response['signals']}")
                else:
                    print(f"Failed to send: {payload} | Status Code: {response.status_code}")

            time.sleep(1)  # Wait before sending the next batch

if __name__ == "__main__":
    generate_random_traffic_data()
