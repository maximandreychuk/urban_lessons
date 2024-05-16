"""Сложная задача./Сдача всем."""

price_for_kg = int(input("Введите цену за килограмм:"))
weight = int(input("Вес:"))
money = int(input("Сколько денег:"))

if money-(price_for_kg*weight)<1: print("Не хватает немного")
else: print(f"Ваша сдача:{money-(price_for_kg*weight)}")