class Car():
    price = 10000

    def horse_powers(self):
        return 1

    def __str__(self):
        return f"Авто {self.__class__.__name__}, Цена {self.price}, Силы {self.horse_powers()}"


class Nissan(Car):
    price = 16000

    def horse_powers(self):
        return 99


class Kia(Car):
    price = 11000

    def horse_powers(self):
        return 64


n = Nissan()
k = Kia()
print(n)
print(k)
