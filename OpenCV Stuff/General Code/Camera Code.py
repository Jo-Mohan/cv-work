import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    cv.imshow('frame', frame[:,::-1])
    
    if cv.waitKey(1) == ord(' '):
        break