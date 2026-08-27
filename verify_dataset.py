import os

image_dir = "train/PS-RGB_tiled"
label_dir = "train/geojson_aircraft_tiled"

images = {
    os.path.splitext(f)[0]
    for f in os.listdir(image_dir)
    if f.endswith(".png")
}

labels = {
    os.path.splitext(f)[0]
    for f in os.listdir(label_dir)
    if f.endswith(".geojson")
}

print("Images:", len(images))
print("Labels:", len(labels))
print("Images without labels:", len(images - labels))
print("Labels without images:", len(labels - images))
print("Matched pairs:", len(images & labels))

