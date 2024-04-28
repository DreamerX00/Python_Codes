import cv2 
import mediapipe as mp
import pyautogui
import time

def count_fingers(lst):
    cnt = 0

    thresh = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2

    if (lst.landmark[5].y*100 - lst.landmark[8].y*100) > thresh:
        cnt += 1

    if (lst.landmark[9].y*100 - lst.landmark[12].y*100) > thresh:
        cnt += 1

    if (lst.landmark[13].y*100 - lst.landmark[16].y*100) > thresh:
        cnt += 1

    if (lst.landmark[17].y*100 - lst.landmark[20].y*100) > thresh:
        cnt += 1

    if (lst.landmark[5].x*100 - lst.landmark[4].x*100) > 6:
        cnt += 1

    return cnt 

cap = cv2.VideoCapture(0)

drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
face_mesh = mp.solutions.face_mesh
hand_obj = hands.Hands(max_num_hands=10) #Adjust the number of hands as needed
face_mesh_obj = face_mesh.FaceMesh(max_num_faces=10)  # Adjust the number of faces as needed

start_init = False 
prev = -1

while True:
    end_time = time.time()
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)

    # Face mesh detection
    frm_rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)
    face_results = face_mesh_obj.process(frm_rgb)

    if face_results.multi_face_landmarks:
        for face_landmarks in face_results.multi_face_landmarks:
            drawing.draw_landmarks(
                image=frm,
                landmark_list=face_landmarks,
                connections=face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                connection_drawing_spec=drawing.DrawingSpec(color=(0, 255, 0), thickness=1)
            )

    # Hand detection
    res = hand_obj.process(frm_rgb)

    if res.multi_hand_landmarks:
        for hand_landmarks in res.multi_hand_landmarks:
            cnt = count_fingers(hand_landmarks)

            if not(prev==cnt):
                if not(start_init):
                    start_time = time.time()
                    start_init = True

                elif (end_time-start_time) > 0.2:
                    if (cnt == 1):
                        pyautogui.press("right")
                    elif (cnt == 2):
                        pyautogui.press("left")
                    elif (cnt == 3):
                        pyautogui.press("up")
                    elif (cnt == 4):
                        pyautogui.press("down")
                    elif (cnt == 5):
                        pyautogui.press("space")

                    prev = cnt
                    start_init = False

            drawing.draw_landmarks(frm, hand_landmarks, hands.HAND_CONNECTIONS)

    cv2.imshow("window", frm)

    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break
