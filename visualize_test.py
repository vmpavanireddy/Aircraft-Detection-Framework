from PIL import Image, ImageDraw

image_path = "train/PS-RGB_tiled/36_104001003E76E200_tile_92.png"
output_path = "test_bounding_boxes.png"

img = Image.open(image_path).convert("RGB")
draw = ImageDraw.Draw(img)

boxes = [
    (77.9842, 412.1818, 113.9862, 431.5028),
    (133.4272, 416.7420, 177.2296, 437.0231)
]

for i, (xmin, ymin, xmax, ymax) in enumerate(boxes, start=1):
    draw.rectangle(
        [xmin, ymin, xmax, ymax],
        outline="red",
        width=3
    )
    draw.text((xmin, ymin - 15), f"Aircraft {i}", fill="red")

img.save(output_path)

print("Saved:", output_path)
