import cv2 as cv 

cap = cv.VideoCapture(0)

mog = cv.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    fgmask = mog.apply(gray)
    
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    fgmask = cv.erode(fgmask, kernel, iterations=1)
    fgmask = cv.dilate(fgmask, kernel, iterations=1)
    
    contours, hierarchy = cv.findContours(fgmask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Ignore small contours
        if cv.contourArea(contour) < 5000:
            continue
        
        # Draw bounding box around contour
        x, y, w, h = cv.boundingRect(contour)
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv.imshow('Motion Detection', frame[:,::-1])
    if cv.waitKey(1) == ord('q'):
        break
        
cap.release()
cv.destroyAllWindows()