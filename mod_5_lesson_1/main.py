class House():

    def __init__(self):
        self.numberOfFloors = 10


my_house = House()
attr_name = 'numberOfFloors'
if hasattr(my_house, attr_name):
    print("Текущий этаж равен", my_house.numberOfFloors)
