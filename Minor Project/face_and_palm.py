import cv2
import mediapipe as mp
from enum import Enum

class KeyCode(Enum):
    Q = 81
    q = 113

CASCADE_PATH = 'haarcascade_frontalface_default.xml'
FACE_BOX_COLOR = (255, 255, 255)
FACE_BOX_THICKNESS = 2
HAND_BOX_THICKNESS = 2

face_data = cv2.CascadeClassifier(CASCADE_PATH)
cam = cv2.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands(max_num_hands = 90)
Draw = mp.solutions.drawing_utils

try:
    while True:
        success, img = cam.read()

        RGBimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Detect faces
        face_coordinates = face_data.detectMultiScale(RGBimg)

        # Process hands
        results = hands.process(RGBimg)

        # Draw rectangles for faces
        for (x, y, w, h) in face_coordinates:
            cv2.rectangle(img, (x, y), (x + w, y + h), FACE_BOX_COLOR, FACE_BOX_THICKNESS)

        # Display number of hands
        if results.multi_hand_landmarks:
            cv2.putText(img, f"Hands : {len(results.multi_hand_landmarks)}", (10, img.shape[0] - 30), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 165, 0), 2, cv2.LINE_AA)
        # Display number of faces
        cv2.putText(img, f"Faces : {len(face_coordinates)}", (10, img.shape[0] - 10), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Draw landmarks for hands
        if results.multi_hand_landmarks:
            for idx, lnms in enumerate(results.multi_hand_landmarks):
                Draw.draw_landmarks(
                    img,
                    lnms,
                    mphands.HAND_CONNECTIONS,
                    Draw.DrawingSpec(color=(0, 0, 256), thickness=2),
                    Draw.DrawingSpec(color=(35, 247, 11), thickness=HAND_BOX_THICKNESS)
                )

        cv2.imshow("Akash_&_Vikram_Minor_Project", img)
        key = cv2.waitKey(1)

        if key == KeyCode.Q.value or key == KeyCode.q.value:
            break

finally:
    cam.release()
    cv2.destroyAllWindows()
