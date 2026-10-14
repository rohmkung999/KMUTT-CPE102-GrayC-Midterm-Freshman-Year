"""
KMUTT CPE 102 - Engineering Exploration (Midterm Project)
Group: Gray C
Module: Virtual Mapping, Pixel-to-CM Scaling & Color Zone Detector
"""

import cv2
import numpy as np

class ArenaMapper:
    def __init__(self, field_width_cm=200.0, field_height_cm=150.0):
        self.field_width_cm = field_width_cm
        self.field_height_cm = field_height_cm
        self.px_to_cm_ratio = 1.0

    def compute_ratio(self, frame_width_px):
        """Calculates pixel-to-cm ratio."""
        self.px_to_cm_ratio = frame_width_px / self.field_width_cm
        return self.px_to_cm_ratio

    def get_drop_zones(self, frame):
        """
        Detects colored drop-off target zones using HSV thresholding.
        Returns coordinates of color zone centers.
        """
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Color definitions: (Lower HSV, Upper HSV)
        color_ranges = {
            "RED": ([0, 120, 70], [10, 255, 255]),
            "GREEN": ([36, 100, 100], [86, 255, 255]),
            "BLUE": ([94, 80, 2], [126, 255, 255]),
            "YELLOW": ([20, 100, 100], [30, 255, 255])
        }

        targets = {}
        for color_name, (lower, upper) in color_ranges.items():
            mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            if contours:
                c = max(contours, key=cv2.contourArea)
                if cv2.contourArea(c) > 400:  # Minimum area filter
                    M = cv2.moments(c)
                    if M["m00"] != 0:
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                        targets[color_name] = (cX, cY)
                        cv2.circle(frame, (cX, cY), 7, (255, 255, 255), -1)
                        cv2.putText(frame, color_name, (cX - 20, cY - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        return frame, targets

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    mapper = ArenaMapper()

    print("[INFO] KMUTT CPE102 Gray C - Starting Virtual Mapping...")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (800, 600))
        ratio = mapper.compute_ratio(800)
        processed_frame, zones = mapper.get_drop_zones(frame)

        cv2.putText(processed_frame, f"Scale: {ratio:.2f} px/cm", (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("CPE 102 - Arena Virtual Map", processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
