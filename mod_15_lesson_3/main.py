import cv2
import numpy as np

cap = cv2.VideoCapture('eyes.mov')

while True:
    ret, frame = cap.read()
    eyes_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = eyes_cascade.detectMultiScale(
        gray_frame, scaleFactor=1.3, minNeighbors=20)
    for (x, y, w, h) in eyes:
        region_of_interest = frame[y:y+h, x:x+w]
        blurred_region = cv2.GaussianBlur(region_of_interest, (15, 15), 0, 0)
        frame[y:y+h, x:x+w] = blurred_region

    cv2.imshow('res', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
