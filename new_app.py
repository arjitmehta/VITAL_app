from flask import Flask, render_template, Response

import numpy as np
import time
import cv2
from PoseModule import pm  # Assuming PoseModule is a separate file for Pose class

app = Flask(__name__)


class Exercise:
    def __init__(self, name, joint_points, angle_ranges, color=(255, 0, 255)):
        self.name = name
        self.joint_points = joint_points
        self.angle_ranges = angle_ranges
        self.color = color

    def calculate_angle(self, img, detector):
        return detector.findAngle(img, *self.joint_points)

    def calculate_completion(self, angle):
        for angle_range in self.angle_ranges:
            min_angle, max_angle = angle_range
            if min_angle <= angle <= max_angle:
                return 100
        return 0


class YogaPose(Exercise):
    pass


class LiftingExercise(Exercise):
    def __init__(self, name, joint_points, angle_ranges, rep_threshold=0.5, color=(255, 0, 255)):
        super().__init__(name, joint_points, angle_ranges, color)
        self.rep_threshold = rep_threshold
        self.count = 0
        self.dir = 0

    def calculate_rep(self, angle):
        if angle == 100:
            self.color = (0, 255, 0)
            if self.dir == 0:
                self.count += self.rep_threshold
                self.dir = 1
        elif angle == 0:
            self.color = (0, 255, 0)
            if self.dir == 1:
                self.count += self.rep_threshold
                self.dir = 0
        return self.count


def create_exercise(exercise_type, name, joint_points, angle_ranges, **kwargs):
    if exercise_type == "yoga":
        return YogaPose(name, joint_points, angle_ranges)
    elif exercise_type == "lifting":
        return LiftingExercise(name, joint_points, angle_ranges, **kwargs)
    else:
        raise ValueError("Invalid exercise type")

exercises = {
    "beg_1": create_exercise("yoga", "Yoga Beginner Pose 1", (15, 13, 11), [(...)]),
    # ... Define other yoga and lifting exercises here
}


def main():
    detector = pm.poseDetector()
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)

        if len(lmList) != 0:
            # Get exercise name from external source (e.g., user input)
            exercise_name = "ex_1"  # Replace with actual exercise name
            exercise = exercises.get(exercise_name)

            if exercise:
                angle = exercise.calculate_angle(img, detector)
                completion = exercise.calculate_completion(angle)

                # Draw exercise info on the frame
                # ...

                if isinstance(exercise, LiftingExercise):
                    rep_count = exercise.calculate_rep(completion)
                    # Draw rep count on the frame
                    # ...

        # ... Rest of the video processing logic (FPS calculation, frame display)

        # ...


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')
def video():
    return Response(main(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
