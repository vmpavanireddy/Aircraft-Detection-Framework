from ultralytics import YOLO

# Load the trained model
model = YOLO(
    "runs/detect/runs/rareplanes_yolo11n_full/weights/best.pt"
)

# Run predictions on a few test images
results = model.predict(
    source="yolo_dataset/images/test",
    imgsz=512,
    conf=0.25,
    device="mps",
    save=True,
    project="runs",
    name="test_predictions",
    max_det=100
)

print("Prediction completed.")
print("Predictions saved in:")
print("runs/detect/test_predictions")
