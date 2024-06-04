"""
Закрепить написание шаблонов с применением регулярных выражений.
Написать программу-поисковик, отслеживающий верные ссылки по заданному шаблону.

Для начала установите виртуальное окружение и зависимости:
python3 -m venv venv   
source venv/bin/activate
pip3 install -r requirements.txt
"""


import re
import requests
from bs4 import BeautifulSoup as bs

URL = 'https://learnodo-newtonic.com/famous-russian-artists'
URL_1 = 'https://gallerix.ru/album/GTG?ysclid=lx09a8fmsm273940725'


def extract_image_links(url):
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    with open('links.txt', 'w') as file:
        lst_art = soup.find_all('img')
        for i in lst_art:
            file.write(f'{i['src']} \n')
    with open('links.txt', 'r') as file:
        for line in file:
            if re.match("(.+?)(?:jpeg|jpg|png|gif)", line):
                print(line)


extract_image_links(URL_1)
