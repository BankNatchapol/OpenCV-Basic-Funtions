import os
import cv2 as cv
import numpy as np

DIR = r'photos/train'

people = []
for p in os.listdir(DIR):
    people.append(p)

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            haar_cascade = cv.CascadeClassifier('haarcascades/haar_face.xml')\

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

            for (x,y,w,h) in faces_rect: 
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training done----------------------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features, labels)

face_recognizer.save('recognizer/face_trained.yml')
np.save('recognizer/features.npy', features)
np.save('recognizer/labels.npy', labels)

print('Labels =', people)
print(f'Length of the labels = {len(labels)}')
print(f'Length of the features = {len(features)}')