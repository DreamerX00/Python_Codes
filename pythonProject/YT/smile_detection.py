import cv2
import numpy as np
import emoji
from cv2 import rectangle

from numpy import True_, true_divide

face_detection = cv2.CascadeClassifier('D:\python\pythonProject\YT\haarcascade_frontalface_default.xml')
smile_detection = cv2.CascadeClassifier('D:\python\pythonProject\YT\haarcascade_smile.xml')

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
        smile_coordinates = smile_detection.detectMultiScale(g2scale,scaleFactor = 1.7,minNeighbors = 10)

        # for (x_, y_, w_, h_) in smile_coordinates:
        #     print('Hey Buddy',smile_coordinates)
        #     cv2.rectangle(face_data,(x_,y_),(x_ + w_ , y_ + h_),(0,0,256),2)
        if len(smile_coordinates) > 0:
            
            cv2.putText(frame,'smiling',(x,y+h-170),fontScale= 1,thickness= 4,fontFace=cv2.LINE_AA, color=(242,184,26))
               

        elif(face_coordinates) > 1000:
                cv2.putText(frame,('Why so serious'),(x,y+h-170),fontScale= 1,thickness= 4,fontFace=cv2.LINE_AA, color=(11,49,239))
                
        else:
            print("0k")
            

    cv2.imshow('smile detect',frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

cam.release()
cv2.destroyAllWindows()



print("Code Complete")