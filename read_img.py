import cv2 as cv

img = cv.imread('photos/plastic.jpeg') # read image

cv.imshow('Plastic', img) # show image 

cv.waitKey(0) # wait for key 0 press
