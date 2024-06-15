"""
Задание:
Частью вашей работы будет сокрытие взгляда при помощи инструментов 
компьютерного зрения и нейронных сетей.


Вся программа должна работать с видеопотоком (не с 1 картинкой).
Для распознавания глаз используйте каскад Хаара, который находится в свободном доступе - GitHub OpenCV.
Глаза должны быть размыты так, чтобы были видны только их очертания (рекомендуется разное размытие по осям x и y)
Область глаз должна быть шире чем сами глаза (как в примере).
Область глаз должна быть чёрно-белого формата (как в примере).
Поставленную задачу можно решить как с применением масок, так и без них.
"""


import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    eyes_cascade = cv2.CascadeClassifier('left_eye.xml')
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eyes_cascade.detectMultiScale(
        gray_frame, scaleFactor=1.3, minNeighbors=20)

    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y + h), (77, 77, 77), 0)
        region_of_interest = frame[y:y+h, x:x+w]
        blurred_region = cv2.GaussianBlur(
            region_of_interest, (77, 77), 77, 77)
        frame[y:y+h, x:x+w] = blurred_region

    cv2.imshow('res', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
