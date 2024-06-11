import cv2
import numpy as np

cap = cv2.VideoCapture('eyes.mov')

while True:
    ret, frame = cap.read()

    y = 0
    x = 0
    h = 200
    w = 200
    region_of_interest = frame[y:y+h, x:x+w]
    blurred_region = cv2.GaussianBlur(frame, (15, 15), 12)
    frame[y:y+h, x:x+w] = blurred_region

    cv2.imshow('res', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
