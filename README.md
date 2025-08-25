# AI Personal Trainer Posture

## Overview
The AI Personal Trainer Posture project aims to provide real-time feedback on posture using computer vision techniques. By leveraging MediaPipe and OpenCV, the application analyzes webcam input to detect body landmarks and assess posture based on predefined rules. The goal is to help users maintain proper posture while sitting or standing.

## Quickstart
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-personal-trainer-posture.git
   cd ai-personal-trainer-posture
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python main.py --camera 0 --min-detection 0.5 --min-tracking 0.5 --model-complexity 1
   ```

## Command-Line Flags
- `--camera`: Specify the camera index (default is 0).
- `--min-detection`: Minimum detection confidence (default is 0.5).
- `--min-tracking`: Minimum tracking confidence (default is 0.5).
- `--model-complexity`: Complexity of the pose model (0, 1, or 2).
- `--no-draw`: Disable drawing landmarks on the output.

## Project Structure
```
ai-personal-trainer-posture/
├── .gitignore
├── LICENSE
├── requirements.txt
├── README.md
├── main.py
├── src/
│   └── posture/
│       ├── __init__.py
│       ├── pose_estimator.py
│       ├── angles.py
│       └── feedback.py
├── scripts/
│   └── benchmark.py
└── tests/
    └── test_angles.py
```

## Architecture & Flow

```
[Webcam Input]
      |
      v
[OpenCV Frame Capture]
      |
      v
[MediaPipe Pose Estimation]
      |
      v
[PoseEstimator (src/posture/pose_estimator.py)]
      |
      v
[Angle Calculations (src/posture/angles.py)]
      |
      v
[PostureFeedbackEngine (src/posture/feedback.py)]
      |
      v
[Overlay Feedback & FPS]
      |
      v
[Display Frame (OpenCV)]
      |
      v
[User Input: q / esc to quit]
```

**Flow Summary:**
1. Capture webcam frames using OpenCV.
2. Detect body landmarks with MediaPipe Pose.
3. Calculate joint angles and tilts.
4. Apply rule-based posture feedback.
5. Overlay cues and FPS on the video.
6. Display output; quit with `q` or `esc`.


## Notes
- Ensure your webcam is accessible and functioning properly.
- The application runs at approximately 20-22 FPS, depending on the system's performance.
- The posture feedback rules include checks for neck flexion, torso tilt, and uneven shoulders, which can be extended as needed.