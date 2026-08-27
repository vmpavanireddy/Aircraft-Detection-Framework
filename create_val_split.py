import os
import shutil
import random

# ---------- SETTINGS ----------

TRAIN_IMAGES = "yolo_dataset/images/train"
TRAIN_LABELS = "yolo_dataset/labels/train"

VAL_IMAGES = "yolo_dataset/images/val"
VAL_LABELS = "yolo_dataset/labels/val"

VAL_RATIO = 0.20
SEED = 42

# ---------- CREATE VALIDATION FOLDERS ----------

os.makedirs(VAL_IMAGES, exist_ok=True)
os.makedirs(VAL_LABELS, exist_ok=True)

# ---------- FIND TRAINING IMAGES ----------

images = [
    f for f in os.listdir(TRAIN_IMAGES)
    if f.endswith(".png")
]

print("Training images found:", len(images))

# ---------- REPRODUCIBLE SHUFFLE ----------

random.seed(SEED)
random.shuffle(images)

# ---------- SELECT VALIDATION IMAGES ----------

val_count = int(len(images) * VAL_RATIO)

val_images = images[:val_count]

print("Validation images:", len(val_images))
print("Remaining training images:", len(images) - len(val_images))

# ---------- COPY IMAGE + MATCHING LABEL ----------

copied = 0
missing_labels = 0

for image_name in val_images:

    base_name = os.path.splitext(image_name)[0]

    image_source = os.path.join(
        TRAIN_IMAGES,
        image_name
    )

    image_destination = os.path.join(
        VAL_IMAGES,
        image_name
    )

    label_source = os.path.join(
        TRAIN_LABELS,
        base_name + ".txt"
    )

    label_destination = os.path.join(
        VAL_LABELS,
        base_name + ".txt"
    )

    if not os.path.exists(label_source):
        print("Missing label:", base_name)
        missing_labels += 1
        continue

    shutil.copy2(
        image_source,
        image_destination
    )

    shutil.copy2(
        label_source,
        label_destination
    )

    copied += 1

print()
print("========== VALIDATION SPLIT COMPLETE ==========")
print("Validation images copied:", copied)
print("Validation labels copied:", copied)
print("Missing labels:", missing_labels)
print("Random seed:", SEED)
print("Validation ratio:", VAL_RATIO)