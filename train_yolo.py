from ultralytics import YOLO

# Load the original pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Full RarePlanes training
results = model.train(
    data="data.yaml",
    epochs=50,
    imgsz=512,
    batch=4,
    device="mps",
    workers=0,
    patience=10,
    project="runs",
    name="rareplanes_yolo11n_full",
    seed=42,
    plots=True
)

print("Full training completed.")
