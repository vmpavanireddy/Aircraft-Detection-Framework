class_mapping = {
    1: 0,  # Small Civil Transport/Utility
    2: 1,  # Medium Civil Transport/Utility
    3: 2,  # Large Civil Transport/Utility
    4: 3,  # Military Transport/Utility/AWAC
    5: 4,  # Military Fighter/Interceptor/Attack
    6: 5,  # Military Trainer
    7: 6   # Military Bomber
}

class_names = [
    "Small Civil Transport/Utility",
    "Medium Civil Transport/Utility",
    "Large Civil Transport/Utility",
    "Military Transport/Utility/AWAC",
    "Military Fighter/Interceptor/Attack",
    "Military Trainer",
    "Military Bomber"
]

for rareplanes_id, yolo_id in class_mapping.items():
    print(
        "RarePlanes ID:",
        rareplanes_id,
        "-> YOLO ID:",
        yolo_id,
        "->",
        class_names[yolo_id]
    )
