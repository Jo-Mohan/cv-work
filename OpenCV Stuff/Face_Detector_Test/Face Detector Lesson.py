from random import randrange as rand 
import cv2 as cv


#face data import
trained_face_data = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')


#capture my video
cap = cv.VideoCapture(0)

#infinitely grab each next frame and apply what is asked
while True:
    ret, frame = cap.read()
    
    
    #take the trained data and interpret the coords of the face detected as x,y,w,h
    face_coords = trained_face_data.detectMultiScale(frame)

    #assign those values found into a built-in rectangle code
    for (x,y,w,h) in face_coords:
     cv.rectangle(frame, (x,y), (x+w, y+h), (rand(256),0,0), (3))

    # Display the resulting frame
    cv.imshow('frame', frame[:,::-1])
    if cv.waitKey(1) == ord(' '):
        break
    
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()