class Car():
    price = 10000
    horses = 10

    def horse_powers(self):
        pass

    def __str__(self):
        return f"Класс {self.__class__.__name__} Цена {self.price}, {self.horse_powers()}"


class Nissan(Car):
    price = 16000
    horses = 99

    def horse_powers(self):
        return f'{self.horses} - это силы первого автомобиля'


class Kia(Car):
    price = 11000
    horses = 64

    def horse_powers(self):
        return f'{self.horses} - это силы второго автомобиля'


n = Nissan()
k = Kia()
print(n)
print(k)
