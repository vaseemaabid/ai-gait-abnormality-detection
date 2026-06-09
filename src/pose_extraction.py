
import cv2
import mediapipe as mp
import csv

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

video = cv2.VideoCapture("walking_video.mp4")

with open("keypoints.csv", "w", newline="") as file:

    writer = csv.writer(file)

    while video.isOpened():

        success, frame = video.read()

        if not success:
            break

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = pose.process(rgb)

        if results.pose_landmarks:

            row = []

            for landmark in results.pose_landmarks.landmark:

                row.extend([
                    landmark.x,
                    landmark.y,
                    landmark.z
                ])

            writer.writerow(row)

video.release()
