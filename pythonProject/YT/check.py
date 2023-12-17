import cv2


classifier_file='D:\python\pythonProject\YT\cars.xml'
# #our image
# car_images='E:\programs\python project\car and pedistian detector\video.mp4'

#load some pre trained data 
car_tracker= cv2.CascadeClassifier(classifier_file)#cascade means a long chain of hard feature that we goung to run into  and classifier means its classifing something as a pedistian or a car or anything 

#create opencv image 
webcam=cv2.VideoCapture('D:\python\pythonProject\YT\media\cars2.mp4')
while True:
      successful_frame_read,cars=webcam.read()

      gray_img=cv2.cvtColor(cars,cv2.COLOR_BGR2GRAY)#changing the color to gray scale

      car_coordinates=car_tracker.detectMultiScale(gray_img)

      for(x,y,w,h) in car_coordinates:
       cv2.rectangle(cars,(x,y),(x+w,y+h),(0,255,0),4)

      #it will show the image
      cv2.imshow('car detector',cars)

      key=cv2.waitKey(1)#it will hold the image as used earlier

      if(key==81 or key==113):
        break


webcam.release()
print("code complete")