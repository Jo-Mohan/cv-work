import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

answer = input('What color do you want to search for (Red, Green, Blue, Brown):')

while True:
    ret, frame = cap.read()


    #convert to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    #range of blue
    lower_blue = np.array([94,80,2])
    upper_blue = np.array([126,255,255])
    blue_mask = cv.inRange(hsv, lower_blue, upper_blue)

    #range of green 
    lower_green = np.array([25,52,72])
    upper_green = np.array([102,255,255])
    green_mask = cv.inRange(hsv, lower_green, upper_green)

    #range of red
    lower_red = np.array([161,155,84])
    upper_red = np.array([179,255,255])
    red_mask = cv.inRange(hsv, lower_red, upper_red)

    #range of brown
    lower_brown = np.array([0,30,53])
    upper_brown = np.array([20,180,255])
    brown_mask = cv.inRange(hsv, lower_brown, upper_brown)

    if answer.lower()=="red":
    # Bitwise-AND mask and original image
        output = cv.bitwise_and(frame,frame, mask= red_mask)
        cv.imshow('Red Frame', output[:,::-1])

    elif answer.lower()=="green":
    # Bitwise-AND mask and original image
        output = cv.bitwise_and(frame,frame, mask= green_mask)
        cv.imshow('Green Frame', output[:,::-1])

    elif answer.lower()=="blue":
    # Bitwise-AND mask and original image
        output = cv.bitwise_and(frame,frame, mask= blue_mask)
        cv.imshow('Blue Frame', output[:,::-1])
    
    elif answer.lower()=="brown":
    # Bitwise-AND mask and original image
        output = cv.bitwise_and(frame,frame, mask= brown_mask)
        cv.imshow('Brown Frame', output[:,::-1])

    else:
        print("Not a color we can detect try again")
        answer = input('What color do you want to search for (Red, Green, Blue, Brown):')

    #Comment code out below to check normal camera
    #cv.imshow('frame', frame[:,::-1])
    if cv.waitKey(1) == ord(' '):
        break




