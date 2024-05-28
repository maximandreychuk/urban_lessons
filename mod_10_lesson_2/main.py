"""
Инструкции:
Напишите программу с использованием механизмов многопоточности, которая создает два потока-рыцаря.

Каждый рыцарь должен иметь имя (name) и умение(skill). 
Умение рыцаря определяет, сколько времени потребуется рыцарю, 
чтобы выполнить свою защитную миссию для королевства.
Враги будут нападать в количестве 100 человек. 
Каждый день рыцарь может ослабить вражеское войско на skill-человек.
Если у рыцаря skill равен 20, то защищать крепость он будет 5 дней (5 секунд в программе).
Чем выше умение, тем быстрее рыцарь защитит королевство.
"""


import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill
        self.enemy = 100

    def run(self):
        chill = self.enemy/self.skill
        print(f"{self.name}, на нас напали!")
        for i in range(int(chill)):
            self.enemy -= self.skill
            time.sleep(1)
            print(
                f"{self.name} сражается {i+1} дней , осталось {self.enemy} воинов!")
        self.enemy = 100
        print(f"{self.name} одержал победу спустя {int(chill)} дней!")


knight1 = Knight("Картер Грейсон", 10)
knight2 = Knight("Келси Уинслоу", 25)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print(f"Все битвы закончились!")
