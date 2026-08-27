import os

TRAIN_IMAGES = "yolo_dataset/images/train"
TRAIN_LABELS = "yolo_dataset/labels/train"

VAL_IMAGES = "yolo_dataset/images/val"
VAL_LABELS = "yolo_dataset/labels/val"

removed_images = 0
removed_labels = 0

# Get validation filenames
val_images = [
    f for f in os.listdir(VAL_IMAGES)
    if f.endswith(".png")
]

print("Validation images found:", len(val_images))

for image_name in val_images:

    base_name = os.path.splitext(image_name)[0]

    train_image = os.path.join(
        TRAIN_IMAGES,
        image_name
    )

    train_label = os.path.join(
        TRAIN_LABELS,
        base_name + ".txt"
    )

    # Remove matching training image
    if os.path.exists(train_image):
        os.remove(train_image)
        removed_images += 1

    # Remove matching training label
    if os.path.exists(train_label):
        os.remove(train_label)
        removed_labels += 1

print()
print("========== REMOVAL COMPLETE ==========")
print("Training images removed:", removed_images)
print("Training labels removed:", removed_labels)
