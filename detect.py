import argparse
from ultralytics import YOLO
import os

def run_detection(source, model_path="yolov8n.pt", save=True):
    # Load model
    model = YOLO(model_path)

    # Run inference
    results = model(source, save=save, project="outputs", name="yolov8_results")

    print(f"Detection completed. Results saved in outputs/yolov8_results/")
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv8 Object Detection")
    parser.add_argument('--source', type=str, required=True,
                        help='Image or video path or webcam id (0 for default camera)')
    parser.add_argument('--model', type=str, default="yolov8n.pt",
                        help='Path to YOLOv8 model weights (default: yolov8n.pt)')
    args = parser.parse_args()

    run_detection(args.source, args.model)
