
from ultralytics import YOLO

# Load the best model from the completed training run
model = YOLO(
    "runs/detect/runs/rareplanes_yolo11n_full/weights/best.pt"
)

print("Best model loaded successfully.")
print("Running final evaluation on the TEST set...")

results = model.val(
    data="data.yaml",
    split="test",
    imgsz=512,
    batch=4,
    device="mps",
    plots=True
)

print("\n========== FINAL TEST EVALUATION COMPLETE ==========")
