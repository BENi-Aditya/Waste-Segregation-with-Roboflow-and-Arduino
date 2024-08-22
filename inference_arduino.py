from roboflow import Roboflow
import cv2
import serial
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set your API key and model ID
api_key = os.getenv("ROBOFLOW_API_KEY")
model_id = os.getenv("MODEL_ID")

# Initialize Roboflow
rf = Roboflow(api_key=api_key)

# Load the pre-trained model
project = rf.workspace().project("plastic-recyclable-detection")
model = project.version(1).model

# Initialize serial communication with Arduino
serial_device_name = '/dev/cu.usbserial-2110'  # Replace with your correct serial port
try:
    arduino = serial.Serial(serial_device_name, 9600)
    time.sleep(2)  # Allow time for the connection to establish
    print("Serial connection established")
except serial.SerialException as e:
    print(f"Error connecting to serial device: {e}")
    exit(1)

def send_serial_command(command):
    try:
        arduino.write(command.encode())
        time.sleep(4)  # Allow time for the servo to move, hold position, and return to neutral
        print(f"Sent command: {command}")
    except serial.SerialException as e:
        print(f"Error sending command: {e}")

# Initialize the camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference on the frame
    results = model.predict(frame, confidence=40, overlap=30).json()['predictions']

    # Process the results
    detections = []
    for result in results:
        label = result['class']
        confidence = result['confidence']
        x, y, w, h = result['x'], result['y'], result['width'], result['height']
        detections.append({
            "label": label,
            "confidence": confidence,
            "bbox": [x, y, w, h]
        })

    # Annotate the frame with inference results
    for detection in detections:
        label = detection["label"]
        confidence = detection["confidence"]
        x, y, w, h = detection["bbox"]

        # Draw bounding box
        pt1 = (int(x - w/2), int(y - h/2))
        pt2 = (int(x + w/2), int(y + h/2))
        cv2.rectangle(frame, pt1, pt2, (0, 255, 0), 2)

        # Draw label
        cv2.putText(frame, f'{label} {confidence:.2f}', (int(x - w/2), int(y - h/2 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Save the annotated frame to disk
    filename = f'output_frame_{frame_count}.jpg'
    cv2.imwrite(filename, frame)
    frame_count += 1

    # Determine type of plastic detected
    for detection in detections:
        label = detection["label"]
        if "PET" in label or "HDP" in label:
            send_serial_command('R')  # Move servo to left for PET/HDP plastic
        else:
            send_serial_command('L')  # Move servo to right for other plastics

    # Use a different key check mechanism for exit
    if frame_count >= 100:  # Stop after 100 frames, adjust as needed
        break

cap.release()
arduino.close()