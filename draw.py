import cv2 as cv
import numpy as np 

blank = np.zeros((500, 500, 3), dtype='uint8') # blank plain
blank[:] = 255,255,255 # change color
cv.imshow('white', blank)


blank = np.zeros((500, 500, 3), dtype='uint8') # blank plain
blank[200:300, 300:400] = 0,0,255 # change pixels on x 300->400, y 200-> 300 from top left
cv.imshow('Rectangle basic', blank)


blank = np.zeros((500, 500, 3), dtype='uint8') # blank plain
# create rectangle box on point (100, 100) to (250, 250), change thickness to cv.FILLED or -1 to fill the box
cv.rectangle(blank, (100, 100), (250, 250), (0,0,255), thickness=2) 
# create circle on center (250, 250) with radius 100, change thickness to cv.FILLED or -1 to fill the box
cv.circle(blank, (250, 250), 100, (0,0,255), thickness=2) 
# create line from (100, 270) to (150, 400), change thickness to cv.FILLED or -1 to fill the box
cv.line(blank, (100, 270), (150, 400), (0,0,255), thickness=2) 
# create text Hello, World at point (200, 400) with FONT_HERSHEY_COMPLEX font, scale font size with 1.0, change thickness to cv.FILLED or -1 to fill the box
cv.putText(blank, 'Hello, World', (200, 400), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), thickness=2) 
cv.imshow('Draw function', blank)

cv.waitKey(0)