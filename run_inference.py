from roboflow import Roboflow
import supervision as sv
import cv2
import time
import os

# Set your API key and model ID
api_key = os.getenv("ROBOFLOW_API_KEY")
model_id = os.getenv("MODEL_ID")

# Initialize Roboflow
rf = Roboflow(api_key=api_key)

# Load the pre-trained model
project = rf.workspace().project("plastic-recyclable-detection")
model = project.version(1).model

# Initialize the camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

# Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Create supervision annotators
bounding_box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()

while True:
    start_time = time.time()
    
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference on the frame
    results = model.predict(frame).json()

    # Load the results into the supervision Detections API
    detections = sv.Detections.from_inference(results)

    # Annotate the frame with inference results
    annotated_frame = bounding_box_annotator.annotate(scene=frame, detections=detections)
    annotated_frame = label_annotator.annotate(scene=annotated_frame, detections=detections)

    # Display the annotated frame
    cv2.imshow('Waste Detection', annotated_frame)

    # Control frame rate
    elapsed_time = time.time() - start_time
    time.sleep(max(1./30 - elapsed_time, 0))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()