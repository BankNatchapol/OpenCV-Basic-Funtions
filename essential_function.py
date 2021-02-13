import cv2 as cv

img = cv.imread('photos/nature.jpg')
cv.imshow('Original', img)

# convert color from BGR to Gray 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur image using gaussian blur (5,5) is kernal, increase kernel size increase bluring
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge cascade, find edge of image, 125 is threshold 1 -> edge line, 175 is threshold 2 -> edge link
canny = cv.Canny(blur, 100, 125)
cv.imshow('Canny Edges', canny)

# Dilating image, increasing line size 
dilated = cv.dilate(canny, (15,15), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding image, decreasing iine size
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Eroded', eroded)

# Resize image into (200,200), interpolation means the way to fill missing valur when increasing size or delete value when decresing size
# if incresing size use cv.INTER_CUBIC, decresing size use cv.INTER_AREA  
resized = cv.resize(img, (200,200), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# crop image from x 200->400, y 50->200
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)