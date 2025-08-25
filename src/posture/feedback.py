class PostureFeedbackEngine:
    def __init__(self):
        self.rules = {
            'neck_flexion': self.check_neck_flexion,
            'torso_tilt': self.check_torso_tilt,
            'uneven_shoulders': self.check_uneven_shoulders
        }

    def check_neck_flexion(self, angle):
        # Implement logic to check neck flexion based on angle
        return angle > 45  # Example threshold

    def check_torso_tilt(self, angle):
        # Implement logic to check torso tilt based on angle
        return angle > 30  # Example threshold

    def check_uneven_shoulders(self, left_angle, right_angle):
        # Implement logic to check for uneven shoulders
        return abs(left_angle - right_angle) > 10  # Example threshold

    def evaluate_posture(self, pose_data):
        feedback = []
        if self.rules['neck_flexion'](pose_data['neck_angle']):
            feedback.append("Adjust your neck posture.")
        if self.rules['torso_tilt'](pose_data['torso_angle']):
            feedback.append("Keep your torso upright.")
        if self.rules['uneven_shoulders'](pose_data['left_shoulder_angle'], pose_data['right_shoulder_angle']):
            feedback.append("Ensure your shoulders are even.")
        return feedback