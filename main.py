import cv2
import mediapipe as mp
import time
import argparse
from src.posture.pose_estimator import PoseEstimator
from src.posture.feedback import PostureFeedbackEngine

def main(camera_index=0, min_detection_conf=0.5, min_tracking_conf=0.5, model_complexity=1, no_draw=False):
    cap = cv2.VideoCapture(camera_index)
    pose_estimator = PoseEstimator(min_detection_conf, min_tracking_conf, model_complexity)
    feedback_engine = PostureFeedbackEngine()

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        start_time = time.time()
        image = pose_estimator.process_image(image)

        if not no_draw:
            pose_estimator.draw_landmarks(image)

        fps = 1 / (time.time() - start_time)
        feedback = feedback_engine.get_feedback(pose_estimator.pose_result)
        
        cv2.putText(image, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(image, feedback, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('Posture Feedback', image)

        if cv2.waitKey(5) & 0xFF in [ord('q'), 27]:  # 'q' or 'esc' to quit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='AI Personal Trainer Posture')
    parser.add_argument('--camera', type=int, default=0, help='Camera index')
    parser.add_argument('--min-detection', type=float, default=0.5, help='Minimum detection confidence')
    parser.add_argument('--min-tracking', type=float, default=0.5, help='Minimum tracking confidence')
    parser.add_argument('--model-complexity', type=int, default=1, help='Model complexity (0, 1, or 2)')
    parser.add_argument('--no-draw', action='store_true', help='Disable drawing landmarks on the image')
    
    args = parser.parse_args()
    main(args.camera, args.min_detection, args.min_tracking, args.model_complexity, args.no_draw)