from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Dictionary to keep track of traffic data for each junction and device
traffic_data = {}


@app.route('/traffic', methods=['POST'])
def handle_traffic():
    data = request.json
    junction_id = data.get('junction_id')
    device_id = data.get('device_id')
    vehicle_count = data.get('vehicle_count')
    air_quality = data.get('air_quality')

    # Update traffic data for this junction and device
    if junction_id not in traffic_data:
        traffic_data[junction_id] = {}
    traffic_data[junction_id][device_id] = {
        'vehicle_count': vehicle_count,
        'air_quality': air_quality
    }

    # Calculate signal timings based on aggregated data
    response = calculate_signal_timings(junction_id)
    return jsonify(response)


def calculate_signal_timings(junction_id):
    # Aggregating vehicle counts from all devices in the junction
    total_vehicles = sum(data['vehicle_count'] for data in traffic_data[junction_id].values())

    signals = {}
    max_green_time = 30  # Max green light time in seconds
    for device_id, data in traffic_data[junction_id].items():
        # Calculate green time proportionally
        green_time = min(max_green_time,
                         (data['vehicle_count'] / total_vehicles) * max_green_time) if total_vehicles > 0 else 0
        red_time = 60 - green_time  # Assuming a total cycle time of 60 seconds for simplicity
        signals[device_id] = {
            'green_time': round(green_time),
            'red_time': round(red_time)
        }

    return {
        'junction_id': junction_id,
        'signals': signals
    }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
