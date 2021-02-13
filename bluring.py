import cv2 as cv

img = cv.imread('photos/nature.jpg')
cv.imshow('Original', img)

# blur is using average bluring method by average surrounding pixel.
avg = cv.blur(img, (7,7))
cv.imshow('Avg', avg)

# Gaussian blur is bluring using kernel weight, 0 is sigmaX is standard deviation in x direction value.
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian', gauss)

# Median blur is using median value in kernel size.
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

# Bilateral blur is bluring using d-> kernel size, sigmaColor-> number of pixel that consider when blur and sigmaSpace-> space that will random choose pixel to consider.
bilateral = cv.bilateralFilter(img, 9, 50, 40)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)