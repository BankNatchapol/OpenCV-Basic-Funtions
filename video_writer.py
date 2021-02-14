import cv2 as cv

capture = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('videos/webcam.avi', fourcc, 20.0, (640,480))

while 1:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
    out.write(gray_bgr)
    cv.imshow('gray', gray_bgr)

    if cv.waitKey(30) & 0xFF == ord('d'):
        break

capture.release()
out.release()
cv.destroyAllWindows()