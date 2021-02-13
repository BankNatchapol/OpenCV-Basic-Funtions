import cv2 as cv

img = cv.imread('photos/nature.jpg')
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# simple thresholding if pixel value greater than 150 it will be 255 else 0
# return threshold is value 150, thresh is image 
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

# inverse thresholding if pixel value greater than 150 it will be 0 else 255
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Threshold Inverse', thresh)

# adaptive thresholding is using block gaussian value as threshold. its will be difference in each block
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3) 
cv.imshow('Adaptive Gaussian', adaptive_thresh)

cv.waitKey(0) 