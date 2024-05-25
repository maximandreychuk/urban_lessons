class Buiding():
    def __init__(self,
                 numberOfFloors: int,
                 buildingType: str) -> None:
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other) -> bool:
        return (self.numberOfFloors == other.numberOfFloors
                and self.buildingType == other.buildingType
                )


my_house = Buiding(2, "Office")
my_house2 = Buiding(2, "Office")
y_house = Buiding(9, "Brick")

print(my_house == my_house2)
print(my_house == y_house)
