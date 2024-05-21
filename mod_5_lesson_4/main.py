class Building():
    total = 0

    def __init__(self):
        Building.total = self.total + 1

    def __str__(self):
        return f"Это {Building.total} объект класса"


for obj in range(40):
    obj = Building()
    print(obj)
