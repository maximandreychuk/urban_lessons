class Vehicle():
    vehicle_type = "none"


class Car():
    price = 1000000

    def horse_powers(self):
        pass


class Nissan(Car, Vehicle):
    vehicle_type = "Sedan"
    price = 16000

    def horse_powers(self):
        return 99


n = Nissan()

print(n.vehicle_type, n.price)
