import cv2 as cv
import numpy as np

img = cv.imread('photos/nature.jpg')
cv.imshow('Original', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 70, 125)
cv.imshow('Canny Edges', canny)

# contours is object shape, it's not much difference from edge.
# find contour return contour matrix to write on blank.
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found.')

blank = np.zeros(img.shape[:2], dtype='uint8')
# draw contour to write contour from find contour.
drawn_contour = cv.drawContours(blank, contours, -1, (255,255,255), 2)
cv.imshow('Contours Drawn', drawn_contour)

cv.waitKey(0)