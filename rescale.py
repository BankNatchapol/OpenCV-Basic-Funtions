import cv2 as cv 


def changeRes(width, height):
    # can use only with live video

    # capture.set set resolution of the live video 
    capture.set(3,width) # 3 is propid = 3 means width
    capture.set(4, height) # 4 is propid = 4 means height

def rescaleFrame(frame, scale=0.75):
    # can use with image, video and live video

    # frame.shape return (width, height) 
    width = int(frame.shape[1] * scale) 
    height = int(frame.shape[0] * scale)

    dimensions = (width, height) # new shape to resize

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



capture = cv.VideoCapture(0) # read video from source if using webcam change path to 0 
changeRes(100, 100)

while True:
    isTrue, frame = capture.read() # read from video return (is there value, binary image value)
    cv.imshow('Me', frame) # show image
    if cv.waitKey(20) == ord('d'): # wait for key press 20 ms
        break

capture.release() # release resources from machine (webcam, memory) 
cv.destroyAllWindows() # destroy video window 


capture = cv.VideoCapture('videos/earth.mp4') # read video from source if using webcam change path to 0 
 
while True:
    isTrue, frame = capture.read() # read from video return (is there value, binary image value)
    frame_rescaled = rescaleFrame(frame, 0.5)

    cv.imshow('Earth', frame) # show image
    cv.imshow('Earth rescaled', frame_rescaled) # show image

    if cv.waitKey(20) == ord('d'): # wait for key press 20 ms
        break

capture.release() # release resources from machine (webcam, memory) 
cv.destroyAllWindows() # destroy video window 

img = cv.imread('photos/steel_bottle.jpeg')

cv.imshow('Steel bottle', img)
cv.imshow('Steel bottle rescaled', rescaleFrame(img))

cv.waitKey(0)