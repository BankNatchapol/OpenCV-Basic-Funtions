import numpy as np 
import cv2 as cv 

haar_cascade = cv.CascadeClassifier('haarcascades/haar_face.xml')

people = ['lisa', 'rose', 'jennie', 'jisoo']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('recognizer/face_trained.yml')