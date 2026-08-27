import json
import os
import shutil
import re
from PIL import Image

# ---------- SETTINGS ----------

IMAGE_DIR = "train/PS-RGB_tiled"
LABEL_DIR = "train/geojson_aircraft_tiled"

OUTPUT_IMAGES = "yolo_dataset/images/train"
OUTPUT_LABELS = "yolo_dataset/labels/train"

CLASS_MAPPING = {
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6
}

# ---------- CREATE OUTPUT FOLDERS ----------

os.makedirs(OUTPUT_IMAGES, exist_ok=True)
os.makedirs(OUTPUT_LABELS, exist_ok=True)

# ---------- COUNTERS ----------

processed = 0
with_aircraft = 0
without_aircraft = 0
errors = 0
total_aircraft = 0

# ---------- FIND ALL PNG IMAGES ----------

image_files = [
    f for f in os.listdir(IMAGE_DIR)
    if f.endswith(".png")
]

print("Images found:", len(image_files))

# ---------- PROCESS EACH IMAGE ----------

for filename in image_files:

    sample_name = filename[:-4]

    image_path = os.path.join(
        IMAGE_DIR,
        filename
    )

    geojson_path = os.path.join(
        LABEL_DIR,
        sample_name + ".geojson"
    )

    aux_path = image_path + ".aux.xml"

    output_image = os.path.join(
        OUTPUT_IMAGES,
        filename
    )

    output_label = os.path.join(
        OUTPUT_LABELS,
        sample_name + ".txt"
    )

    try:

        # ---------- READ IMAGE SIZE ----------

        img = Image.open(image_path)
        image_width, image_height = img.size

        # ---------- READ GEOTRANSFORM ----------

        with open(aux_path, "r") as f:
            aux_content = f.read()

        match = re.search(
            r"<GeoTransform>\s*(.*?)\s*</GeoTransform>",
            aux_content
        )

        if not match:
            raise ValueError("GeoTransform not found")

        geo = [
            float(x)
            for x in match.group(1).split(",")
        ]

        origin_x = geo[0]
        pixel_width = geo[1]
        origin_y = geo[3]
        pixel_height = geo[5]

        # ---------- READ GEOJSON ----------

        with open(geojson_path, "r") as f:
            data = json.load(f)

        yolo_labels = []

        # ---------- CONVERT AIRCRAFT ----------

        for feature in data["features"]:

            role_number = feature["properties"]["role_id"]
            role_name = feature["properties"]["role"]

            if role_number not in CLASS_MAPPING:
                print(
                    "Unknown class:",
                    role_number,
                    role_name,
                    "in",
                    filename
                )
                continue

            class_id = CLASS_MAPPING[role_number]

            coordinates = feature["geometry"]["coordinates"][0]

            pixel_points = []

            for longitude, latitude in coordinates:

                x = (
                    longitude - origin_x
                ) / pixel_width

                y = (
                    latitude - origin_y
                ) / pixel_height

                pixel_points.append((x, y))

            xs = [p[0] for p in pixel_points]
            ys = [p[1] for p in pixel_points]

            xmin = max(0, min(xs))
            xmax = min(image_width, max(xs))

            ymin = max(0, min(ys))
            ymax = min(image_height, max(ys))

            # Skip invalid boxes

            if xmax <= xmin or ymax <= ymin:
                continue

            # ---------- YOLO FORMAT ----------

            x_center = (
                (xmin + xmax) / 2
            ) / image_width

            y_center = (
                (ymin + ymax) / 2
            ) / image_height

            width = (
                xmax - xmin
            ) / image_width

            height = (
                ymax - ymin
            ) / image_height

            yolo_labels.append(
                f"{class_id} "
                f"{x_center:.6f} "
                f"{y_center:.6f} "
                f"{width:.6f} "
                f"{height:.6f}"
            )

        # ---------- SAVE IMAGE ----------

        shutil.copy2(
            image_path,
            output_image
        )

        # ---------- SAVE LABEL ----------

        with open(output_label, "w") as f:
            f.write("\n".join(yolo_labels))

        # ---------- UPDATE COUNTERS ----------

        processed += 1

        if yolo_labels:
            with_aircraft += 1
            total_aircraft += len(yolo_labels)
        else:
            without_aircraft += 1

        # Print progress every 100 images

        if processed % 100 == 0:
            print(
                "Processed:",
                processed,
                "/",
                len(image_files)
            )

    except Exception as e:

        errors += 1

        print(
            "ERROR:",
            filename,
            "->",
            e
        )

# ---------- FINAL REPORT ----------

print()
print("========== CONVERSION COMPLETE ==========")
print("Images found:", len(image_files))
print("Images processed:", processed)
print("Images with aircraft:", with_aircraft)
print("Images without aircraft:", without_aircraft)
print("Total aircraft labels:", total_aircraft)
print("Errors:", errors)