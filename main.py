# main.py

import cv2
import requests
from vehicle_detection import detect_vehicles
from air_quality_sensor import read_air_quality
import time

# Change this to your camera's streaming URL if it's live or use the path to an image.
CAMERA_URL = "http://your_camera_feed_url"  # Replace with the actual URL or use cv2.VideoCapture(0) for a local camera
SERVER_URL = "http://127.0.0.1:5000/traffic"  # your Flask server URL

# Initialize the camera
cap = cv2.VideoCapture(CAMERA_URL)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

try:
    while True:
        # Capture frame from the camera
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Detect vehicles in the frame
        vehicle_count = detect_vehicles(frame)

        # Read air quality data
        air_quality = read_air_quality()

        # Prepare payload for the server
        payload = {
            'vehicle_count': vehicle_count,
            'air_quality': air_quality
        }

        # Send the data to the server
        try:
            response = requests.post(SERVER_URL, json=payload)
            if response.status_code == 200:
                print(f"Data sent successfully: {payload}")
            else:
                print(f"Failed to send data: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error while sending data: {e}")

        # Optional: display the frame with vehicle count
        cv2.putText(frame, f'Vehicles: {vehicle_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Camera', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Sleep for a while before the next iteration to prevent flooding the server
        time.sleep(5)  # Adjust based on your requirements

except KeyboardInterrupt:
    print("Stopped by user.")

finally:
    # Release the camera and destroy all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
