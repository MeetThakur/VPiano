import cv2
import mediapipe as mp
import numpy as np
from pygame import mixer

mixer.init()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def calculate_finger_angle(point1, point2, point3):
    vector1 = np.array([point1.x - point2.x, point1.y - point2.y])
    vector2 = np.array([point3.x - point2.x, point3.y - point2.y])
    cosine_angle = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
    angle = np.arccos(cosine_angle)
    return np.degrees(angle)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=4),
                mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)
            )
            
            finger_landmarks = [
                ("Thumb", [1, 2, 4], 30),
                ("Index", [5, 6, 8], 60),
                ("Middle", [9, 10, 12], 90),
                ("Ring", [13, 14, 16], 120),
                ("Pinky", [17, 18, 20], 150)
            ]
            

            h, w, c = image.shape
            for finger_name, landmarks, y_pos in finger_landmarks:
                angle = calculate_finger_angle(
                    hand_landmarks.landmark[landmarks[0]],
                    hand_landmarks.landmark[landmarks[1]],
                    hand_landmarks.landmark[landmarks[2]]
                )
                
                if finger_name not in globals():
                    globals()[finger_name] = False

                if angle <= 160 and not globals()[finger_name]:
                    mixer.music.load(f"sounds/{finger_landmarks.index((finger_name, landmarks, y_pos)) + 1}.mp3")
                    mixer.music.play(0)
                    globals()[finger_name] = True

                if angle > 160:
                    globals()[finger_name] = False
                

                if 160 < angle < 180:
                    cv2.putText(image, f"{finger_name}: Slightly Bent", (10, y_pos), 
                              cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                elif angle <= 160:
                    cv2.putText(image, f"{finger_name}: Bent", (10, y_pos), 
                              cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                else:
                    cv2.putText(image, f"{finger_name}: Straight", (10, y_pos), 
                              cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            
            for id, landmark in enumerate(hand_landmarks.landmark):
                h, w, c = image.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                if id == 0:
                    cv2.circle(image, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
    
    cv2.imshow('Hand Tracking', image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()