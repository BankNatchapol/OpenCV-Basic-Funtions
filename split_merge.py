import cv2 as cv
import numpy as np

img = cv.imread('photos/nature.jpg')
cv.imshow('Original', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# split image channel from (x, y, 3) into 3 (x, y)
b, g, r = cv.split(img)

# merge 3 channel to make color appear
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

cv.waitKey(0)