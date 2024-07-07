from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Image as IMG
import cv2
import numpy as np
from PIL import Image
from .detection import classes
from django.shortcuts import redirect


def index(request):
    all_images = IMG.objects.all()
    return render(request, 'base.html', {'all_images': all_images})


def get_users_images(request):
    users_images = IMG.objects.filter(user=request.user)
    return render(request, 'findobj/my_images.html', {'users_images': users_images})


def detection(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['myfile1']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        # file_url = fs.url(filename)

        model = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt.txt',
                                         'MobileNetSSD_deploy.caffemodel')
        image = cv2.imread(f'findobj/media/loads/{filename}')
        resized_image = cv2.resize(image, (300, 300))
        blob = cv2.dnn.blobFromImage(
            resized_image, 0.007843, (300, 300), 127.5)
        model.setInput(blob)
        detections = model.forward()
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                class_id = int(detections[0, 0, i, 1])
                class_name = classes[class_id]
                box = detections[0, 0, i, 3:7] * \
                    np.array([image.shape[1], image.shape[0],
                              image.shape[1], image.shape[0]])
                (startX, startY, endX, endY) = box.astype('int')
                cv2.rectangle(image, (startX, startY),
                              (endX, endY), (0, 255, 0), 2)
                label = '{}: {:.2f}%'.format(class_name, confidence * 100)
                cv2.putText(image, label, (startX, startY - 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        im = Image.fromarray(image)
        im.save(f'findobj/media/loads/{filename}')
        res_image = IMG.objects.create(image=filename,
                                       user=request.user,
                                       confidence=label)
        res_image.save()
        return render(request, 'findobj/result.html', {
            'res_image': res_image
        })
    return render(request, 'findobj/add_image.html')


def delete(request, pk):
    img = IMG.objects.filter(id=pk)
    img.delete()
    return redirect('get_users_images')
