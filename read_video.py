import cv2 as cv

capture = cv.VideoCapture('videos/earth.mp4') # read video from source if using webcam change path to 0 
 
while True:
    isTrue, frame = capture.read() # read from video return (is there value, binary image value)
    cv.imshow('Earth', frame) # show image

    if cv.waitKey(20) == ord('d'): # wait for key press 20 ms
        break

capture.release() # release resources from machine (webcam, memory) 
cv.destroyAllWindows() # destroy video window 