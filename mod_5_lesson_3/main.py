class Buiding():
    def __init__(self,
                 numberOfFloors: int,
                 buildingType: str) -> None:
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)

    def __eq__(self,) -> bool:
        return self.numberOfFloors == self.buildingType


my_house = Buiding(2, "2")

if my_house.__eq__():
    print('похожи')
