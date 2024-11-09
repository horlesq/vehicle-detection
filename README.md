# Vehicle Detection

This project is a vehicle detection application using the YOLOv5 deep learning model to identify and display bounding boxes around vehicles in a video stream. The application can detect cars, motorcycles, buses, and trucks, drawing bounding boxes around each detected vehicle in real-time.

![2024-11-0909-58-00-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/a7a5b675-7f64-46ee-a11e-0c94abf85e99)


## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [License](#license)
- [Contact](#contact)


## Features

- **Real-time Detection**: Detects and draws bounding boxes around vehicles (cars, motorcycles, buses, trucks) in video frames.
- **YOLOv5 Model Integration**: Utilizes the YOLOv5s model for efficient and accurate vehicle detection.
- **Customizable Detection Classes**: Easily adjustable to detect other object classes as needed.


## Technologies

- **Computer Vision**: OpenCV for video frame processing and display.
- **Deep Learning**: PyTorch for utilizing YOLOv5 model weights and performing real-time detection.
- **YOLOv5 Model**: Pre-trained YOLOv5s model from Ultralytics for object detection.

## Installation

To get started with this project, follow these steps:
1. **Clone the repository**:
```bash
git clone https://github.com/horlesq/vehicle-detection.git
```
2. **Navigate to the project directory**:
```bash
cd vehicle-detection
```
3. **Install dependencies:**:
```bash
pip install -r requirements.txt
```
4. **Place your video file** in the data folder within the project directory. Ensure the file path inside main.py matches your file name.
5. **Run the vehicle detection script**:
```bash
python main.py
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any inquiries or feedback, feel free to reach out via:

- Email: adrian.horlescu@gmail.com
- Linkedin [Adrian Horlescu](https://www.linkedin.com/in/adrian-horlescu/)
- GitHub: [Horlesq](https://github.com/horlesq)
