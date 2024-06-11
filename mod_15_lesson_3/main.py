import cv2
import numpy as np

cap = cv2.VideoCapture('eyes.mov')

while True:
    ret, frame = cap.read()
    eyes_cascade = cv2.CascadeClassifier('left_eye.xml')
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eyes_cascade.detectMultiScale(
        gray_frame, scaleFactor=1.3, minNeighbors=20)

    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x-350, y), (x+w, y + h), (77, 77, 77), 0)
        region_of_interest = frame[y:y+h, x-350:x+w]
        blurred_region = cv2.GaussianBlur(
            region_of_interest, (77, 77), 77, 77)
        frame[y:y+h, x-350:x+w] = blurred_region

    cv2.imshow('res', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
