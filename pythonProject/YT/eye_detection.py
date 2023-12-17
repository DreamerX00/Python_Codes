import cv2
import numpy as np
import emoji
from cv2 import rectangle

from numpy import True_, true_divide

face_detection = cv2.CascadeClassifier('D:\python\pythonProject\YT\haarcascade_frontalface_default.xml')
eyes_detection = cv2.CascadeClassifier('D:\python\pythonProject\YT\haarcascade_eye_tree_eyeglasses.xml')

cam = cv2.VideoCapture(0)

while True:
    frame_capture, frame = cam.read()
    gscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = face_detection.detectMultiScale(gscale)
    

    
    for (x,y,w,h) in face_coordinates:

        print(face_coordinates)

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,256,0),2)

        face_data = frame[y:y+h, x:x+w]

        g2scale = cv2.cvtColor(face_data, cv2.COLOR_BGR2GRAY)
        eyes_coordinates = eyes_detection.detectMultiScale(g2scale,scaleFactor = 1.1,minNeighbors = 10)

        # for (x_, y_, w_, h_) in eyes_coordinates:
        #     cv2.rectangle(face_data,(x_,y_),(x_ + w_ , y_ + h_),(0,0,256),2)
            

        
        if len(eyes_coordinates) > 0:
            
            cv2.putText(frame,'X',(x+w-120,y+h-72),fontScale= 1,thickness= 6,fontFace=cv2.LINE_AA, color=(242,184,26))
            cv2.putText(frame,'X',(x+w-50,y+h-72),fontScale= 1,thickness= 6,fontFace=cv2.LINE_AA, color=(242,184,26))  
               

        # else:

        #     if len(face_coordinates) > 0:
        #         cv2.putText(frame,('Why so serious'),(x,y+h-170),fontScale= 1,thickness= 4,fontFace=cv2.LINE_AA, color=(11,49,239))

            

    cv2.imshow('eyes detect',frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

cam.release()
cv2.destroyAllWindows()



print("Code Complete")