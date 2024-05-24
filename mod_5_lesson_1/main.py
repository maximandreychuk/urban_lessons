class House():

    def __init__(self):
        self.numberOfFloors = 10


my_house = House()

for attr in range(1, my_house.numberOfFloors+1):
    print(f"Tекущий этаж равен {attr}")
