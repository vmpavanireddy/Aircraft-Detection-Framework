from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model.train(
    data="data.yaml",
    epochs=1,
    imgsz=512,
    batch=4,
    device="mps",
    project="runs",
    name="sanity_check",
    seed=42
)

print("Sanity check training completed.")
