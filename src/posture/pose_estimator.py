from dataclasses import dataclass
import cv2
import mediapipe as mp

class PoseEstimator:
    def __init__(self, min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=1):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=min_detection_confidence,
                                      min_tracking_confidence=min_tracking_confidence,
                                      model_complexity=model_complexity)
        self.fps = 0

    def estimate_pose(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.pose.process(image_rgb)
        return results

    def update_fps(self, frame_count, elapsed_time):
        if elapsed_time > 0:
            self.fps = frame_count / elapsed_time

@dataclass
class PoseResult:
    landmarks: list
    fps: float
    image_shape: tuple

    def __post_init__(self):
        self.landmarks = self.landmarks or []  # Ensure landmarks is a list even if None is passed
        self.image_shape = self.image_shape or (0, 0)  # Default to (0, 0) if None is passed