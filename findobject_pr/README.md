# Курсовой проект Object Detection

Веб приложение на базе фреймворка Django, которое позволит пользователям применять предобученную модель для обнаружения и классификации объектов на фото.
Для доступа к приложению требуется пройти регистрацию и авторизацию, чтобы пользователи могли создавать аккаунты и видеть только собственноручно загруженные изображения. Для интерфейса используется Bootstrap.

К использованию предлагается модель MobileNet SSD. Она определяет следующие классы:
"background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"

## Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone <repo.git>
cd findobject_pr
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
```

Установить зависимости из файла requirements.txt(pip3 если MacOS):

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
