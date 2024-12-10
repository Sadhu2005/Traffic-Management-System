# server.py
from flask import Flask, request, jsonify
import numpy as np
import pandas as pd

app = Flask(__name__)

# Store data (for demonstration purposes)
traffic_data = []


@app.route('/traffic', methods=['POST'])
def handle_traffic():
    data = request.json
    vehicle_count = data.get('vehicle_count')
    air_quality = data.get('air_quality')

    # Process data
    traffic_data.append((vehicle_count, air_quality))
    response = calculate_signal_times(vehicle_count)
    return jsonify(response)


def calculate_signal_times(vehicle_count):
    # Logic to determine signal times based on vehicle count
    red_light_time = max(10, vehicle_count * 2)
    green_light_time = min(120, max(20, 120 - vehicle_count))
    return {'red': red_light_time, 'green': green_light_time}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
