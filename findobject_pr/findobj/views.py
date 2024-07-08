from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Image as IMG
import cv2
import numpy as np
from PIL import Image
from .utils import classes
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

        net = cv2.dnn.readNetFromCaffe('findobj/MobileNetSSD_deploy.prototxt.txt',
                                       'findobj/MobileNetSSD_deploy.caffemodel')
        cv2_image = cv2.imread(f'findobj/media/loads/{filename}')
        LABEL_COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

        (h, w) = cv2_image.shape[:2]
        resized = cv2.resize(cv2_image, (300, 300))
        blob = cv2.dnn.blobFromImage(resized, 0.007843, (300, 300), 127.5)

        net.setInput(blob)
        detections = net.forward()
        conf = 0.2
        vis = cv2_image.copy()
        result = []
        cls = []
        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence != 0.0:
                result.append(confidence)

            if confidence > conf:
                idx = int(detections[0, 0, i, 1])
                cls.append(classes[idx])
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                cv2.rectangle(vis, (startX, startY),
                              (endX, endY), LABEL_COLORS[idx], 1)
                y = startY - 10 if startY - 10 > 10 else startY + 10
                cv2.putText(vis, "{} : {:.2f}%".format(
                    classes[idx], confidence * 100), (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, LABEL_COLORS[idx], 2)

        title = 'result'

        if type(vis) == list:
            if type(title) == list:
                titles = title
            else:
                titles = []

                for i in range(len(vis)):
                    titles.append(title)

            for i in range(len(vis)):
                if len(vis[i].shape) <= 2:
                    rgbImg = cv2.cvtColor(vis[i], cv2.COLOR_GRAY2RGB)
                else:
                    rgbImg = cv2.cvtColor(vis[i], cv2.COLOR_BGR2RGB)

        else:
            if len(vis.shape) < 3:
                rgbImg = cv2.cvtColor(vis, cv2.COLOR_GRAY2RGB)
            else:
                rgbImg = cv2.cvtColor(vis, cv2.COLOR_BGR2RGB)

            im = Image.fromarray(rgbImg)
            im.save(f'findobj/media/loads/{filename}')
        answer = []
        counter = 0
        if cls != []:
            while counter < len(cls):
                answer.append(
                    f'Объект: {cls[counter]}, точность - {round(result[counter]*100,2)}')
                counter += 1
        else:
            answer = 'Объект не найден'

        res_image = IMG.objects.create(image=filename,
                                       user=request.user,
                                       confidence=answer)
        res_image.save()
        return render(request, 'findobj/result.html', {
            'res_image': res_image
        })
    return render(request, 'findobj/add_image.html')


def delete(request, pk):
    img = IMG.objects.filter(id=pk)
    img.delete()
    return redirect('get_users_images')
