"""
Задание:
Напишите программу, которая создает два потока.
Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
Оба потока должны работать параллельно.
"""


import string
import time
from threading import Thread


numbers = [i for i in range(11)]
letters = list(string.ascii_letters[:10])


def get_someone(args):
    for i in range(0, len(args)):
        print(args[i], flush=True)
        time.sleep(1)


thr1 = Thread(target=get_someone, args=[numbers])
thr1.start()

get_someone(letters)

thr1.join()
