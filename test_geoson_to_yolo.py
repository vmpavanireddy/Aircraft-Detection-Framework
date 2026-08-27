import json

geojson_file = "train/geojson_aircraft_tiled/36_104001003E76E200_tile_92.geojson"

# GeoTransform values from the .aux.xml file
origin_x = -1.7599649674358162
pixel_width = 3.4020483117129356e-06
origin_y = 52.818388381928443
pixel_height = -3.4020483117129356e-06

# Image dimensions
image_width = 512
image_height = 512

with open(geojson_file, "r") as f:
    data = json.load(f)

for feature in data["features"]:
    role = feature["properties"]["role"]
    role_id = feature["properties"]["role_id"]

    coordinates = feature["geometry"]["coordinates"][0]

    pixel_points = []

    for longitude, latitude in coordinates:
        x = (longitude - origin_x) / pixel_width
        y = (latitude - origin_y) / pixel_height

        pixel_points.append((x, y))

    xs = [point[0] for point in pixel_points]
    ys = [point[1] for point in pixel_points]

    xmin = max(0, min(xs))
    xmax = min(image_width, max(xs))
    ymin = max(0, min(ys))
    ymax = min(image_height, max(ys))

    x_center = ((xmin + xmax) / 2) / image_width
    y_center = ((ymin + ymax) / 2) / image_height
    width = (xmax - xmin) / image_width
    height = (ymax - ymin) / image_height

    print("Class:", role)
    print("Role ID:", role_id)
    print("Pixel bounding box:")
    print("xmin =", xmin)
    print("ymin =", ymin)
    print("xmax =", xmax)
    print("ymax =", ymax)

    print("\nYOLO format:")
    print(role_id, x_center, y_center, width, height)
