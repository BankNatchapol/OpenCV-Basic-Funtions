import cv2 as cv

img = cv.imread('photos/train/lisa/1.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cascade classifier get xml haarcascade file 
haar_cascade = cv.CascadeClassifier('haarcascades/haar_face.xml')\
# get bounding box of face 
# scaleFactor : specifying how much the image size is reduced at each image scale
# minNeighbors : specifying how many neighbors each candidate rectangle should have to retain it.
# the less minNeighbors the more noisey
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Lisa Detected Faces', img)

group_img = cv.imread('photos/blackpink/jennie_jisoo_lisa_rose.jpg')
group_gray = cv.cvtColor(group_img, cv.COLOR_BGR2GRAY)

group_haar_cascade = cv.CascadeClassifier('haarcascades/haar_face.xml')
group_faces_rect = group_haar_cascade.detectMultiScale(group_gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(group_faces_rect)}')

for (x, y, w, h) in group_faces_rect:
    cv.rectangle(group_img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Blackpink Detected Faces', group_img)

cv.waitKey(0)