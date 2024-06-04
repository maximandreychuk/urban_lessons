"""
Создайте класс SuperDate, наследованный от класса datetime модуля datetime, 
объекты которого будут дополнительно обладать следующими методами:

1. get_season - должен возвращать сезон года (Summer, Autumn, Winter, Spring)
2. get_time_of_day - должен возвращать  время суток.
"""


from datetime import datetime, time
import time


class SuperDate(datetime):
    time_of_day = {
        "Morning": range(6, 12),
        "Day": range(12, 18),
        "Evening": range(18, 24),
        "Night": range(0, 6)
    }

    def __init__(self, year, month, day, hour) -> None:
        self.date = datetime(year, month, day, hour)

    def get_season(self):
        if self.month in range(3, 6):
            return "Spring"
        elif self.month in range(6, 9):
            return "Summer"
        elif self.month in range(9, 12):
            return "Autumn"
        else:
            return "Winter"

    def get_time_of_day(self):
        if self.day in range(6, 12):
            return "Morning"
        elif self.day in range(13, 18):
            return "Day"
        elif self.day in range(18, 23):
            return "Evening"
        else:
            return "Night"


s = SuperDate(2024, 1, 17, 10)
print(s.get_season())
print(s.get_time_of_day())
