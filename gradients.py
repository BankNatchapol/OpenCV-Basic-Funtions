import cv2 as cv
import numpy as np

img = cv.imread('photos/nature.jpg')
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# laplacian is to calculate gradient of image
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap)) # because of gradient can be negative so do absolute
cv.imshow('Laplacing', lap)

# sobel x is to create gradient with x axis
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
# sobel y is to create gradient with y axis
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
# combined x and y sobel 
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)
cv.waitKey(0)
