from ultralytics import YOLO

model = YOLO("yolo11n.pt")

print("Model loaded successfully.")

print("\nRunning dataset validation...")

results = model.val(
    data="data.yaml",
    split="val",
    imgsz=512,
    batch=1,
    plots=False
)

print("\nDataset check completed.")
