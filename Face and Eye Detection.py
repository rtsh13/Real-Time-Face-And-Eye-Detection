#Import the libraries
import numpy
import cv2

#Get the Access to the video cam
capture = cv2.VideoCapture(0)

"""
Haar feature-based cascade classifiers defined for the face and eye detection 
Arguments : cascade classifier,xml file 
"""

face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

while True:
    ret, frame = capture.read()
    #Convert the frame to grayscale because it works better
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Detects objects of different sizes in the input image which in our case is face/Arguments:(grayscaled image,scale_factor,min_neighbors)
    faces = face.detectMultiScale(gray,1.3,5)

    #When the face is detected, detect the eyes only in the face, draw the rectangle around them
    for (x,y,w,h) in faces:
        #Draw the rectanegle for the face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)
        roi_gray = gray[y:y+w , x:x+w]
        roi_color = frame[y:y+h, x:x+w ]
        #detect the Eye using the multiscale classifier
        eye = eye_cascade.detectMultiScale(roi_gray,1.3,5)
        for (ex,ey,ew,eh) in eye:
            cv2.rectangle(roi_color, (ex,ey),(ex+ew,ey+eh),(0,255,0),5)

    #Display the face and eye detected
    cv2.imshow('Frame',frame)
    #Don't exit unless the c key is pressed
    if cv2.waitKey(1) == ord('c'):
        break

#Release the access to video camera and destroy the windows
cap.release()
cv2.destroyAllWindows()

