import cv2
import numpy as np
from PIL import Image
import time
from findobject_pr.settings import MEDIA_ROOT
# classes = ['background', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat',
#            'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse',
#            'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
#            'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove',
#            'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon',
#            'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut',
#            'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse',
#            'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book',
#            'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']
classes = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]


#     model = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt.txt',
#                                      'MobileNetSSD_deploy.caffemodel')
#     image = cv2.imread(pic)
#     resized_image = cv2.resize(image, (300, 300))
#     blob = cv2.dnn.blobFromImage(resized_image, 0.007843, (300, 300), 127.5)
#     model.setInput(blob)
#     detections = model.forward()
#     for i in range(detections.shape[2]):
#         confidence = detections[0, 0, i, 2]
#         if confidence > 0.5:
#             class_id = int(detections[0, 0, i, 1])
#             class_name = classes[class_id]
#             box = detections[0, 0, i, 3:7] * \
#                 np.array([image.shape[1], image.shape[0],
#                           image.shape[1], image.shape[0]])
#             (startX, startY, endX, endY) = box.astype('int')
#             cv2.rectangle(image, (startX, startY),
#                           (endX, endY), (0, 255, 0), 2)
#             label = '{}: {:.2f}%'.format(class_name, confidence * 100)
#             cv2.putText(image, label, (startX, startY - 15),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     im = Image.fromarray(image)
#     im.save(f'/media/results/{time.time()}.jpg')


# # pic = '2.jpg'
# pic = cv2.imread('media/2.jpg')
# print(pic.shape)
# # foo('2.jpg')
