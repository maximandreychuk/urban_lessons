"""Работа со списками."""
my_list = ["Orange", "Banane", "Leamon", "Apple", "Mandarine"]
print(my_list)
print(f"Первый - {my_list[0]} и последний элемент - {my_list[-1]}")
print(f"Элементы с третьего по пятый - {my_list[2:5]}")
my_list[2] = "Qiwi"
print(f"Изменился третий элемент: {my_list}")

"""Работа со словарями."""
my_dict = {"RU": 1, "ENG": 2, "DE": 3, "FR": 4, "GBR": 5}
print("Словарь:", my_dict)
print(f"Вывод элемента FR: ", my_dict["FR"])
my_dict.update({"IT": 6})
print("Словарь с добавленным элементом:", my_dict)
