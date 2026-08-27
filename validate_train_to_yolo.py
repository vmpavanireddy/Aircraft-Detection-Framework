import os

IMAGE_DIR = "yolo_dataset/images/train"
LABEL_DIR = "yolo_dataset/labels/train"

images = {
    os.path.splitext(f)[0]
    for f in os.listdir(IMAGE_DIR)
    if f.endswith(".png")
}

labels = {
    os.path.splitext(f)[0]
    for f in os.listdir(LABEL_DIR)
    if f.endswith(".txt")
}

print("Images:", len(images))
print("Labels:", len(labels))

images_without_labels = images - labels
labels_without_images = labels - images

print("Images without labels:", len(images_without_labels))
print("Labels without images:", len(labels_without_images))

# ---------- CHECK LABEL CONTENT ----------

valid_classes = set(range(7))

total_boxes = 0
invalid_lines = 0
invalid_classes = 0
invalid_values = 0

for filename in os.listdir(LABEL_DIR):

    if not filename.endswith(".txt"):
        continue

    path = os.path.join(LABEL_DIR, filename)

    with open(path, "r") as f:
        lines = f.readlines()

    for line_number, line in enumerate(lines, 1):

        line = line.strip()

        if not line:
            continue

        parts = line.split()

        if len(parts) != 5:
            invalid_lines += 1
            print(
                "Invalid format:",
                filename,
                "line",
                line_number
            )
            continue

        try:
            class_id = int(parts[0])
            values = [float(x) for x in parts[1:]]
        except ValueError:
            invalid_lines += 1
            print(
                "Invalid number:",
                filename,
                "line",
                line_number
            )
            continue

        total_boxes += 1

        if class_id not in valid_classes:
            invalid_classes += 1
            print(
                "Invalid class:",
                filename,
                "line",
                line_number,
                "class:",
                class_id
            )

        if not all(0 <= x <= 1 for x in values):
            invalid_values += 1
            print(
                "Invalid YOLO values:",
                filename,
                "line",
                line_number
            )

print()
print("========== VALIDATION ==========")
print("Total bounding boxes:", total_boxes)
print("Invalid lines:", invalid_lines)
print("Invalid classes:", invalid_classes)
print("Invalid YOLO values:", invalid_values)