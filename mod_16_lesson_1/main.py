"""
Техническое задание:
Программа должна считывать данные с сайта CoinMarketCap.
Для парсинга и запросов разрешено использовать любую из перечисленных библиотек: 
requests, selenium, beautifulsoup, scrapy.
Ваш код должен выполнять следующий функционал:
Считывать данные с сайта: название криптовалюты, текущая рыночная капитализация
Записывать данные в CSV файл в следующем порядке: название криптовалюты, 
текущая рыночная капитализация, процент от общей капитализации топ-100 криптовалют.
4.Процент одной криптовалюты должен рассчитывать по первым 100 криптовалютам на странице.
5.Разделитель между столбцами в CSV файле - пробелы.
6.Каждый следующий файл при записи должен иметь название в следующем формате: H.M dd.mm.yyyy, 
где H - Часы, M-минуты, dd- день, mm-месяц, yyyy-год.
"""


import csv
import lxml
import time
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime


def write_cmc_top():
    url = 'https://coinmarketcap.com/ru/'
    response = requests.get(url).text
    soup = bs(response, 'lxml')
    coins = soup.find(
        'table', class_='sc-ae0cff98-3 ipWPGi cmc-table').find('tbody').find_all('tr')
    links = []
    name_list = []
    cap_list = []

    for coin in coins:
        if len(links) < 100:
            links.append(url + coin.find(class_='cmc-link').get('href')[4:])

    for link in links:
        # time.sleep(random.randint(1, 5))
        resp = requests.get(link).text
        sp = bs(resp, 'lxml')
        try:
            coins_name = sp.find(
                class_='sc-d1ede7e3-0 bEFegK').text.split('(')[0][5:-1]
        except AttributeError:
            coins_name = 'Coin'
        html_code_with_capital = str(sp.find('dd', class_='sc-d1ede7e3-0 hPHvUM base-text',
                                             ))[-30:]
        capital = int("".join([str(s)
                               for s in html_code_with_capital if s.isdigit()]))
        name_list.append(coins_name)
        cap_list.append(capital)
        summa = sum(cap_list)

    with open(f'{datetime.now().strftime("%H:%M %d.%m.%Y")}.csv', 'w', newline='') as out_csv:
        writer = csv.writer(out_csv, delimiter=" ", lineterminator="\r")
        writer.writerow(['Name', 'MC', 'MP'])
        counter = 0
        for _ in range(len(name_list)):
            writer.writerow([
                name_list[counter], cap_list[counter], f'{round(cap_list[counter]/summa*100)}%'])
            counter += 1


write_cmc_top()
