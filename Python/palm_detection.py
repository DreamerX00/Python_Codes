import cv2

import mediapipe as mp

import time

cam = cv2.VideoCapture(0)

mphands = mp.solutions.hands

hands = mphands.Hands()

Draw = mp.solutions.drawing_utils

while True:
    success, img = cam.read()

    RGBimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    results = hands.process(RGBimg)
    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for lnms in results.multi_hand_landmarks:
            Draw.draw_landmarks(
            img,
            lnms,
            mphands.HAND_CONNECTIONS,
            Draw.DrawingSpec(color = (0,0,256), thickness= 2),
            Draw.DrawingSpec(color = (35,247,11), thickness= 3)
            )


    cv2.imshow("Damn Bro",img)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

cam.release()
cv2.destroyAllWindows()
