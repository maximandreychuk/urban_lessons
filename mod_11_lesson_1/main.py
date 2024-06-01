"""
Цель:
Познакомиться с использованием сторонних библиотек в Python и применить их в различных задачах.

Для начала установите виртуальное окружение и зависимости:
python3 -m venv venv   
source venv/bin/activate
pip3 install -r requirements.txt
"""


from PIL import Image, ImageFilter
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


url3 = 'https://api.github.com'
print(requests.get(url3).content.decode('utf-8'))
print(requests.get(url3).status_code)


with open('example_50kb.csv') as emm:
    df = pd.read_csv(emm, index_col=0)
    print(df.head(10))


a = np.random.rand(20)
for i in a:
    i += 1
print(a)


plt.plot(a-1, (a+2)**2)
plt.show()


url = "http://www.artlib.ru/objects/gallery_676/artlib_gallery-338391-b.jpg"
im = Image.open(requests.get(url, stream=True).raw)
blurred_jelly = im.filter(ImageFilter.SHARPEN)
blurred_jelly.save("test.jpg")
