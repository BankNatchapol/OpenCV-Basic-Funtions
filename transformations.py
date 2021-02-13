import cv2 as cv
import numpy as np 

img = cv.imread('photos/glass.jpeg')
cv.imshow('Glass', img)

def translate(img, x, y):
    # Create shifting Matrix 
    # M = [[1, 0, x],
    #      [0, 1, y]]
    # -x -> left
    # -y -> up
    # x -> right 
    # y -> down 
    transMat = np.float32([[1,0,x],[0,1,y]])
    # Image dimension
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

def rotate(img, angle, rotPoint=None):
    # Rotate image with angle, at rotPoint
    (height, width) = img.shape[:2]
    
    # if not specify rotation point, using center 
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    # create rotation matrix 
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


translated = translate(img, 100, 100) # shifting image to right 100, down 100
cv.imshow('Translated', translated)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

flip = cv.flip(img, -1) # flipping image with flip code, 0 is horizontal flip, 1 is vertical flip, -1 is horizontal + vertical flip
cv.imshow('Flip', flip)

cv.waitKey(0)