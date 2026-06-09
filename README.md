# AI-Based Gait Abnormality Detection

An AI-powered system that detects gait abnormalities from walking videos using MediaPipe Pose, OpenCV, and Machine Learning techniques.

## Technologies Used

- Python
- OpenCV
- MediaPipe Pose
- Scikit-learn
- Google Colab
- Jupyter Notebook

## Performance

| Metric           | Value                   |
| ---------------- | ----------------------- |
| Dataset Size     | 500+ Samples            |
| Accuracy         | 92%                     |
| Models Evaluated | Random Forest, SVM, KNN |

## Development Tools

- Google Colab
- Jupyter Notebook
- GitHub

## Project Workflow

1. Collected walking video samples.
2. Extracted 33 body keypoints using MediaPipe Pose.
3. Processed video frames using OpenCV.
4. Generated gait-related features.
5. Trained Random Forest, SVM, and KNN models.
6. Evaluated model performance and selected the best classifier.

## Repository Structure

src/
├── pose_extraction.py
├── train_model.py

data/
models/
results/

## Future Improvements

- Real-time webcam gait analysis
- Deep Learning based classification
- Mobile healthcare application
- Cloud-based monitoring dashboard
