from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Store data from devices
device_data = {}


@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    device_id = data['device_id']
    device_data[device_id] = {
        "vehicle_count": data['vehicle_count'],
        "air_quality": data['air_quality']
    }
    return jsonify({"message": "Data received"}), 200


@app.route('/signal', methods=['GET'])
def send_signal():
    # Example signal calculation
    total_vehicles = sum(d["vehicle_count"] for d in device_data.values())
    green_time = [round((d["vehicle_count"] / total_vehicles) * 30) for d in device_data.values()]

    signal = {
        "red_time": 30 - max(green_time),
        "yellow_time": 3,
        "green_time": max(green_time)
    }
    return jsonify(signal), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
