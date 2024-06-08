import cv2
import numpy as np

cap = cv2.VideoCapture('eyes.mov')

while True:
    ret, frame = cap.read()
    eyes_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    x = 1200
    y = 800
    w = 2000
    h = 1800
    cv2.rectangle(frame, (x, y), (x+w, y+h), (52, 60, 62), -1)
    src = frame[y:y+h, x:x+w]
    blurred_region = cv2.GaussianBlur(src, (99, 99), 15, 1)
    frame[y:y+h, x:x+w] = blurred_region

    # eyes = eyes_cascade.detectMultiScale(
    #     gray_frame, scaleFactor=1.3, minNeighbors=20)
    # for (x, y, w, h) in eyes:
    # x = x+250
    # cv2.rectangle(frame, (x, y), (x-3*w, y+h), (52, 60, 62), -1)
    # src = frame[y:y+h, x:x-3*w]
    # blurred_region = cv2.GaussianBlur(src, (15, 15), cv2.BORDER_DEFAULT)
    # frame[y:y+h, x:x-3*w] = blurred_region

    cv2.imshow('res', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
