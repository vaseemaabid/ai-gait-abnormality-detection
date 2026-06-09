# AI-Based Gait Abnormality Detection

An AI-powered system that detects gait abnormalities from walking videos using MediaPipe Pose, OpenCV, and Machine Learning techniques.

## Problem Statement

People with gait abnormalities may suffer from neurological, orthopedic, or movement-related disorders. Manual gait assessment can be time-consuming and subjective. This project automates gait analysis using computer vision and machine learning techniques.

## Technologies Used

### Programming Language
- Python

### Computer Vision
- OpenCV
- MediaPipe Pose

### Machine Learning
- Scikit-learn
- Random Forest
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)

### Development Tools
- Google Colab
- Jupyter Notebook
- GitHub

## Features

- Human Pose Estimation
- Extraction of 33 Body Keypoints
- Video Processing using OpenCV
- Feature Engineering
- Machine Learning Classification
- Gait Abnormality Detection

## Performance

| Metric | Value |
|----------|----------|
| Dataset Size | 500+ Samples |
| Accuracy | 92% |
| Models Evaluated | Random Forest, SVM, KNN |

## Project Workflow

1. Collected walking video samples.
2. Extracted 33 body keypoints using MediaPipe Pose.
3. Processed video frames using OpenCV.
4. Generated gait-related features.
5. Trained Random Forest, SVM, and KNN models.
6. Evaluated model performance and selected the best classifier.

## Repository Structure

```text
ai-gait-abnormality-detection/

├── data/
│   └── README.md

├── models/
│   └── README.md

├── results/
│   ├── README.md
│   └── project_results.md

├── src/
│   ├── pose_extraction.py
│   └── train_model.py

├── requirements.txt
└── README.md
```

## Results

- Successfully extracted pose landmarks using MediaPipe Pose.
- Processed walking videos and generated gait features.
- Trained Random Forest, SVM, and KNN classifiers.
- Achieved 92% classification accuracy on the evaluation dataset.

## Future Improvements

- Real-time webcam gait analysis
- Deep Learning based classification
- Mobile healthcare application
- Cloud-based monitoring dashboard
- Integration with hospital monitoring systems

## Author

**Mahammad Vaseem Aabid**

- B.Tech Computer Science and Engineering
- VIT-AP University
- Aspiring Software Development Engineer
