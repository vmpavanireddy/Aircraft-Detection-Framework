import os

TRAIN_IMAGES = "yolo_dataset/images/train"
TRAIN_LABELS = "yolo_dataset/labels/train"

VAL_IMAGES = "yolo_dataset/images/val"
VAL_LABELS = "yolo_dataset/labels/val"

TEST_IMAGES = "yolo_dataset/images/test"
TEST_LABELS = "yolo_dataset/labels/test"

train_images = {
    os.path.splitext(f)[0]
    for f in os.listdir(TRAIN_IMAGES)
    if f.endswith(".png")
}

val_images = {
    os.path.splitext(f)[0]
    for f in os.listdir(VAL_IMAGES)
    if f.endswith(".png")
}

test_images = {
    os.path.splitext(f)[0]
    for f in os.listdir(TEST_IMAGES)
    if f.endswith(".png")
}

print("Train images:", len(train_images))
print("Validation images:", len(val_images))
print("Test images:", len(test_images))

print()
print("Train ∩ Validation:", len(train_images & val_images))
print("Train ∩ Test:", len(train_images & test_images))
print("Validation ∩ Test:", len(val_images & test_images))

print()
print("Validation images without labels:",
      len(val_images - {
          os.path.splitext(f)[0]
          for f in os.listdir(VAL_LABELS)
          if f.endswith(".txt")
      }))

print("Validation labels without images:",
      len({
          os.path.splitext(f)[0]
          for f in os.listdir(VAL_LABELS)
          if f.endswith(".txt")
      } - val_images))
