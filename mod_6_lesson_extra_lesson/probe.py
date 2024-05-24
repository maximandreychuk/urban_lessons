class Figure():
    sides_count = 0

    def __init__(self, *sides: int) -> None:
        if len(sides) != self.sides_count:
            self.__sides = [1*self.sides_count]
        else:
            self.__sides = [i for i in sides]

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, sides):
        res = []
        for i in sides:
            if i > 0:
                res.append(i)
        if len(res) > 0 and len(sides) == len(self.__sides):
            return True
        else:
            return False

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = sides

    def __str__(self):
        return f"Стороны {self.__sides}"


class Cube(Figure):
    sides_count = 12

    def __sides(self):
        if len(self.__sides) != 1:
            self.__sides == [self.__sides for i in range(self.sides_count)]
        else:
            self.__sides = [1*self.sides_count]

    def get_volume(self):
        return "не умею пока"


c = Circle(14)
c.set_sides(15)  # Изменится
print(c.get_sides())
c.set_sides(11, 11)
print(c.get_sides())
print(len(c))
