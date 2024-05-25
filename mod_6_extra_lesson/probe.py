class Figure():
    sides_count = 0

    def __init__(self, color: tuple, *sides: int, filled: bool = True) -> None:
        if len(sides) != self.sides_count:
            self.__sides = [1*self.sides_count]
        else:
            self.__sides = [i for i in sides]
        self.__color = color
        self.filled = filled

    def get_sides(self):
        return self.__sides


class Cube(Figure):
    sides_count = 12

    def __init__(self, color,  *sides: int, filled: bool = True):
        super().__init__(color, *sides, filled)
        if len(sides) == 1:
            self.__sides = self.sides_count*[i for i in sides]
        else:
            self.__sides = [1*self.sides_count]


cube1 = Cube((132, 14, 15), 6)
print(cube1.get_sides())
