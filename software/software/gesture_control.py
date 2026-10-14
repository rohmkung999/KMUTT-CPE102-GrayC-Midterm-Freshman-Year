"""
KMUTT CPE 102 - Engineering Exploration (Midterm Project)
Group: Gray C
Module: MediaPipe Hand Gesture Control (Manual Override System)
"""

import cv2
import mediapipe as mp

def run_gesture_control():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    print("[INFO] KMUTT CPE102 Gray C - Gesture Control Ready.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        action = "IDLE / AUTO"
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Tip landmarks: Index = 8, Thumb = 4
                index_tip_y = hand_landmarks.landmark[8].y
                index_mcp_y = hand_landmarks.landmark[5].y

                if index_tip_y < index_mcp_y:
                    action = "MANUAL OVERRIDE: INTAKE ACTIVE"
                else:
                    action = "MANUAL OVERRIDE: STOP"

        cv2.putText(frame, f"State: {action}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.imshow("CPE 102 - Gesture Override", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_gesture_control()
