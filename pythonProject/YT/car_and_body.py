import cv2

cars_file = 'D:\python\pythonProject\YT\cars.xml'

body_file = 'D:\python\pythonProject\YT\haarcascade_fullbody.xml'

Car_data = cv2.CascadeClassifier(cars_file)
full_body = cv2.CascadeClassifier(body_file)

# webcam = cv2.imread('D:\python\pythonProject\YT\Images\instagram4.jpg')

webcam = cv2.VideoCapture('D:\python\pythonProject\YT\media\cars2.mp4')

while True:

        frame_capture, frame = webcam.read()


        gscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        car_coordinates = Car_data.detectMultiScale(gscale_frame)
        body_coordinate = full_body.detectMultiScale(gscale_frame)

        for (x,y,w,h) in body_coordinate:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,256),(2))


        for (x,y,w,h) in car_coordinates:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,256,0),(2))

        cv2.imshow('Face Detector',frame)

        key = cv2.waitKey(1)


        if key == 81 or key == 113:
            break

webcam.release()
cv2.destroyAllWindows()

print("Code Complete")