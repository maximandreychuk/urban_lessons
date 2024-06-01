from PIL import Image
import requests


url = "http://www.artlib.ru/objects/gallery_676/artlib_gallery-338391-b.jpg"
im = Image.open(requests.get(url, stream=True).raw)
im.save("test.jpg")

url3 = 'https://api.github.com'


print(requests.get(url3).content.decode('utf-8'))
print(requests.get(url3).status_code)
