from gettext import install

from random import randrange

import cv2
from numpy import True_
face_data = cv2.CascadeClassifier('D:\python\pythonProject\YT\haarcascade_frontalface_default.xml')

# webcam = cv2.imread('D:\python\pythonProject\YT\Images\instagram4.jpg')

webcam = cv2.VideoCapture('group.jpg')

while True:

    frame_capture, frame = webcam.read()


    gscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    face_coordinates = face_data.detectMultiScale(gscale_frame)


    for (x,y,w,h) in face_coordinates:
        print(face_coordinates)
        cv2.rectangle(frame,(x,y),(x+w, y+h), (randrange(1000), randrange(1000), randrange(1000)), randrange(2,5))

    cv2.imshow('Face Detector',frame)

    key = cv2.waitKey(0)

    if key == 81 or key == 113:
        break


webcam.release()
cv2.destroyAllWindows()

print("Code Complete")