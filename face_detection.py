import cv2 as cv

img = cv.imread('photos/lisa/1.jpeg')
cv.imshow('Lisa', img)

cv.waitKey(0)