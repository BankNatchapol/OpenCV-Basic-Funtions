import cv2 as cv
import numpy as np

img = cv.imread('photos/plastic.jpeg')
img = cv.resize(img, (500, 500))
cv.imshow('Original', img)

# Create mask shape
blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[2]//2 + 150), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (img.shape[1]//2 - 50, img.shape[2] + 100), (img.shape[1]//2 + 50, img.shape[2]//2 + 400) , 255, -1)
mask = cv.bitwise_or(circle, rectangle)
cv.imshow('Circle', circle)
cv.imshow('Rectangle', rectangle)
cv.imshow('Mask', mask)

# masking with original image with mask parameter
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask', masked)

cv.waitKey(0)