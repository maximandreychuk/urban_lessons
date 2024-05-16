"""«Работаем с выводом данных»."""

name = input("Название товара: ")
price_for_kg = int(input("Введите цену за килограмм: "))
weight = int(input("Вес: "))
money = int(input("Сколько денег: "))

print("Чек: ")
print(f"Название товара: {name}")
print(f"Вес товара {name}: {weight}")
print(f"Цена за килограмм:{price_for_kg}")
print(f"Итого:{price_for_kg*weight}")
print(f"Внесено: {money}")
print(f"Сдача: {money-(price_for_kg*weight)}")