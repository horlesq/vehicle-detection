import torch
import cv2

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Video capture
video_path = 'data/sample_video_2.mp4'
cap = cv2.VideoCapture(video_path)

# Class IDs and labels - Car, Motorcycle, Bus, Truck
vehicle_classes = {2, 3, 5, 7}

# Process frames
while cap.isOpened():
    # Read the next frame
    ret, frame = cap.read()
    if not ret:
        break
    
    # Run YOLOv5 detection
    results = model(frame)
    
    # Get detections as numpy array [x1, y1, x2, y2, confidence, class]
    detections = results.xyxy[0].cpu().numpy()
    
    # Filter detections to include only vehicles
    for *box, conf, cls in detections:
        if int(cls) in vehicle_classes:
            # Draw a bounding box around the vehicle
            x1, y1, x2, y2 = box
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 127, 255), 2)

    # Display video
    cv2.imshow('Vehicle Detection', frame)
    if cv2.waitKey(1) & 0xFF == 27: # Press 'escape' to exit
        break
    
cap.release()
cv2.destroyAllWindows()