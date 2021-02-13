import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/nature.jpg')
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# histogram is useful when you want to analyze image brightness or color 
# calcHist calculate histogram of image  
# [gray] is image, [0] is channel to calculate histogram (grayscale have only 1), mask if you want to calculate in specify position
# [256] is bins size, [0,256] is histogram ranges
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# plot histogram by color
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()
