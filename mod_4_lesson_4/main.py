class House():
    def __init__(self, numberOfFloors=0):
        self.numberOfFloors = numberOfFloors

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f"В этом доме {floors} этажей")


my_house = House()

my_house.setNewNumberOfFloors(12)
