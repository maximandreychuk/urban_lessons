import cv2
import numpy as np


# img = np.random.rand(300, 300)
img = np.zeros((300, 300, 3), dtype='uint8')
cv2.circle(img, (img.shape[1]//2, img.shape[1]//2),
           125, (255, 255, 255), thickness=3)
cv2.ellipse(img, (img.shape[1]//2, img.shape[1]//2),
            (20, 30), 0, 0, 180, (93, 217, 51), 3)
cv2.ellipse(img, (img.shape[1]//2, img.shape[1]//2),
            (50, 70), 0, 0, 180, (93, 217, 51), 3)
cv2.line(img, (100, 150), (100, 100), color=(217, 52, 58), thickness=3)
cv2.line(img, (130, 150), (130, 100), color=(217, 52, 58), thickness=3)
cv2.line(img, (170, 150), (170, 100), color=(217, 52, 58), thickness=3)
cv2.line(img, (200, 150), (200, 100), color=(217, 52, 58), thickness=3)
cv2.line(img, (100, 100), (130, 100), color=(92, 52, 217), thickness=3)
cv2.line(img, (170, 100), (200, 100), color=(92, 52, 217), thickness=3)

cv2.imshow("TEST", img)
cv2.waitKey(0)
cv2.waitKey(1)
