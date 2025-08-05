# YOLOv8 Object Detection 🚀

This project demonstrates object detection using the **YOLOv8** model from the `ultralytics` library. It supports images, videos, and webcam input.

---

## 📁 Project Structure

yolov8/
├── detect.py # Main script for object detection
├── sample/ # Folder containing test image(s)
│ └── test.jpg
├── outputs/ # Results saved here after detection
├── yolov8n.pt # YOLOv8 nano model (downloaded automatically or manually)
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## 🛠️ Dependencies

- Python 3.8 or higher
- Ultralytics YOLOv8 (`ultralytics` library)

Install dependencies with:

```bash
pip install -r requirements.txt
```
---

## 🚀 How to Run

1. Run on an Image
```bash
python detect.py --source sample/test.jpg
```
2. Run on a Video
```bash
python detect.py --source path/to/video.mp4
```
3. Run on Webcam (default camera)
```bash
python detect.py --source 0
```
The results will be saved in outputs/yolov8_results/.

---

## Input

<p align="center">
  <img src="sample/test.jpg" width="700"/>
</p>

---

## output

<p align="center">
  <img src="outputs/yolov8_results/test.jpg" width="700"/>
</p>

---

##🌍 Impact

Object detection is a cornerstone of modern computer vision with applications across industries. This project leverages YOLOv8, one of the most efficient and accurate object detection models, to enable real-time detection of multiple objects in images, videos, or live webcam feeds.

By demonstrating a lightweight, modular pipeline using YOLOv8, this project empowers developers, students, and researchers to integrate cutting-edge computer vision into their own applications — all with minimal setup.

---

##💼 Use Cases

This object detection system can be adapted for:

Security & Surveillance
Detect intrusions, weapons, or unusual activities in real-time CCTV feeds.

Retail & Inventory Monitoring
Track product availability, customer footfall, or shelf status using camera feeds.

Autonomous Vehicles & Traffic Monitoring
Identify vehicles, pedestrians, and traffic signals for smart city or autonomous car systems.

Healthcare
Detect medical tools in operation theaters or track patient movements.

Wildlife Monitoring & Conservation
Use drones or stationary cameras to detect animals in forests or sanctuaries.

Smart Farming
Detect crops, pests, or livestock from drone or ground-level images.
