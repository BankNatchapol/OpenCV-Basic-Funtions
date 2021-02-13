import cv2
print(cv2.__version__)

img = cv2.imread("photos/glass.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

