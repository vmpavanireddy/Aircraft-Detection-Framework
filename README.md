# ✈️ Aircraft Detection Framework

An AI-based computer vision project for detecting and analyzing aircraft in remote sensing imagery using YOLO and the RarePlanes dataset.

## 📌 Overview

This project explores aircraft detection from aerial and remote sensing images using deep learning and object detection techniques.

The workflow focuses on preparing the dataset, converting annotations into YOLO format, training an object detection model, validating the dataset, and evaluating the trained model on test images.

## 🎯 Project Objectives

- Detect aircraft in remote sensing imagery
- Prepare and validate aircraft detection datasets
- Convert dataset annotations into YOLO-compatible format
- Train a YOLO object detection model
- Evaluate the trained model on test data
- Visualize detection and evaluation results

## 🧠 Aircraft Categories

The project works with seven aircraft categories:

- Small Civil Transport / Utility
- Medium Civil Transport / Utility
- Large Civil Transport / Utility
- Military Transport / Utility / AWAC
- Military Fighter / Interceptor / Attack
- Military Trainer
- Military Bomber

## 🔄 Project Workflow

```text
Remote Sensing Images
        ↓
Dataset Preparation
        ↓
Annotation Conversion
        ↓
YOLO Dataset Validation
        ↓
Model Training
        ↓
Test Image Prediction
        ↓
Model Evaluation
        ↓
Visualization & Analysis
```

## 🛠️ Technologies & Tools

- Python
- YOLO
- Ultralytics
- Computer Vision
- Object Detection
- Remote Sensing Images
- RarePlanes Dataset

## 📂 Project Structure

```text
Aircraft-Detection-Framework/
│
├── analyze_test_classes.py
├── analyzze_classes.py
├── check_yolo_dataset.py
├── class_mapping.py
├── covert_test_to_yolo.py
├── covert_to_yolo.py
├── create_val_split.py
├── evaluate_test.py
├── predict_test_img.py
├── remove_val_from_train.py
├── test_geoson_to_yolo.py
├── test_metadata.py
├── test_training.py
├── train_yolo.py
├── validate_test_to_yolo.py
├── validate_train_to_yolo.py
├── verify_dataset.py
├── verify_val_split.py
└── visualize_test.py
```

## 🏋️ Model Training

The training pipeline uses an Ultralytics YOLO model and trains it on the prepared RarePlanes dataset.

The training configuration includes:

- **Model:** YOLO11 Nano
- **Training Epochs:** 50
- **Image Size:** 512 × 512
- **Batch Size:** 4
- **Early Stopping Patience:** 10 epochs
- **Random Seed:** 42

## 📊 Evaluation

After training, the best model checkpoint is loaded and evaluated on the test split.

The evaluation workflow generates plots that can be used to analyze the model's detection performance.

## 🔍 What I Learned

Through this project, I gained practical exposure to:

- Object detection workflows
- Dataset preparation and validation
- YOLO annotation formats
- Image preprocessing
- Model training and evaluation
- Dataset class mapping
- Test-set prediction
- Computer vision with Python
- Working with remote sensing imagery

## 🚀 Future Improvements

Possible areas for further exploration include:

- Improving detection performance on small aircraft
- Experimenting with different YOLO architectures
- Hyperparameter tuning
- Data augmentation
- Comparing model performance across different configurations
- Improving visualization and analysis of detection results
