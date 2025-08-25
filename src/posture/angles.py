def angle_3pts(pt1, pt2, pt3):
    import numpy as np

    # Calculate the angle between three points
    v1 = np.array(pt1) - np.array(pt2)
    v2 = np.array(pt3) - np.array(pt2)
    angle = np.arctan2(v2[1], v2[0]) - np.arctan2(v1[1], v1[0])
    angle = np.degrees(angle) % 360
    return angle

def vertical_tilt_deg(shoulder_left, shoulder_right, hip_left, hip_right):
    import numpy as np

    # Calculate the vertical tilt based on shoulder and hip positions
    shoulder_mid = (shoulder_left[1] + shoulder_right[1]) / 2
    hip_mid = (hip_left[1] + hip_right[1]) / 2
    tilt = shoulder_mid - hip_mid
    return np.degrees(np.arctan(tilt))