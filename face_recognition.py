import numpy as np 
import cv2 as cv 

haar_cascade = cv.CascadeClassifier('haarcascades/haar_face.xml')

people = ['lisa', 'rose', 'jennie', 'jisoo']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('recognizer/face_trained.yml')

img = cv.imread('photos/blackpink/lisa_rose.jpg')
cv.imshow('Target',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (x,y), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=1)

cv.imshow('Detected Faces', img)

cv.waitKey(0)