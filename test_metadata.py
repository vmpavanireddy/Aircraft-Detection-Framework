import re

aux_file = "train/PS-RGB_tiled/36_104001003E76E200_tile_92.png.aux.xml"

with open(aux_file, "r") as f:
    content = f.read()

match = re.search(r"<GeoTransform>\s*(.*?)\s*</GeoTransform>", content)

if match:
    values = [float(x) for x in match.group(1).split(",")]

    print("GeoTransform values:")
    for i, value in enumerate(values):
        print(f"{i}: {value}")

else:
    print("GeoTransform not found")
