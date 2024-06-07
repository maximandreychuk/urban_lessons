"""
Подготовьте картинку к обработке для нейросети. 
Нейросеть хорошо воспринимает формы и контрастность. 
Также каждую следующую строку ей будет проще определить, 
если между предыдущей и следующей будет разница в цветах.
"""


import cv2
import numpy as np


img = cv2.imread('color_text.jpg')
new_img = np.zeros(img.shape, dtype='uint8')

img = cv2.Canny(img, 50, 50)
contour, hierarchy = cv2.findContours(
    img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(new_img, contour[1500:2122], -1, (19, 226, 92), 1)
cv2.drawContours(new_img, contour[750:1490], -1, (47, 1, 207), 1)
cv2.drawContours(new_img, contour[0:750], -1, (146, 12, 150), 1)
result_img = cv2.convertScaleAbs(new_img, alpha=1.0)

cv2.imshow("Result", result_img)
cv2.waitKey(0)
cv2.waitKey(1)


# with open('con.txt', 'w') as file:
#     file.write(str(contour))
