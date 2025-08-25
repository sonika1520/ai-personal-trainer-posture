import unittest
from src.posture.angles import angle_3pts, vertical_tilt_deg

class TestAngles(unittest.TestCase):

    def test_angle_3pts(self):
        # Test with known points
        p1 = (0, 0)
        p2 = (1, 1)
        p3 = (2, 0)
        expected_angle = 45.0  # Example expected angle
        result = angle_3pts(p1, p2, p3)
        self.assertAlmostEqual(result, expected_angle, places=1)

    def test_vertical_tilt_deg(self):
        # Test with known points
        shoulder_left = (1, 2)
        shoulder_right = (3, 2)
        head = (2, 4)
        expected_tilt = 0.0  # Example expected tilt
        result = vertical_tilt_deg(shoulder_left, shoulder_right, head)
        self.assertAlmostEqual(result, expected_tilt, places=1)

if __name__ == '__main__':
    unittest.main()