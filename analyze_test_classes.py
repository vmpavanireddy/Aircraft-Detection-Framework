import os
import json
from collections import Counter

label_dir = "test/geojson_aircraft_tiled"

role_counts = Counter()

for filename in os.listdir(label_dir):
    if not filename.endswith(".geojson"):
        continue

    filepath = os.path.join(label_dir, filename)

    with open(filepath, "r") as f:
        data = json.load(f)

    for feature in data.get("features", []):
        properties = feature.get("properties", {})
        role = properties.get("role")

        if role:
            role_counts[role] += 1

print("\nTest aircraft class distribution:\n")

for role, count in role_counts.most_common():
    print(f"{role}: {count}")

print("\nTotal aircraft:", sum(role_counts.values()))
print("Total classes:", len(role_counts))
