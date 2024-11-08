import torch
import cv2

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Video capture
video_path = 'data/sample_video_1.mp4'
cap = cv2.VideoCapture(video_path)

# Process frames
while cap.isOpened():
    # Read the next frame
    ret, frame = cap.read()
    if not ret:
        break
    
    # Run YOLOv5 detection
    results = model(frame)
    
    # Overlay boxes and labels on frame
    results.render()
    
    # Display video
    cv2.imshow('Vehicle Detection', frame)
    if cv2.waitKey(1) & 0xFF == 27: # Press 'escape' to exit
        break
    
cap.release()
cv2.destroyAllWindows()