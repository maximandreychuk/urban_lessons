"""
Задача 1: Фабрика Функций
Написать функцию, которая возвращает различные математические функции 
(например, деление, умножение) в зависимости от переданных аргументов.
"""


def get_numb(sign: str):
    if sign == '*':
        def multiply(a, b):
            return a*b
        return multiply
    elif sign == '/':
        def division(a, b):
            return a/b
        return division
    elif sign == '-':
        def subtraction(a, b):
            return a - b
        return subtraction
    else:
        def addition(a, b):
            return a + b
        return addition


list_of_numbers_1 = [10, 92, 1, 87, 736]
list_of_numbers_2 = [11, 20, 100, 2, 89]
get_sign = get_numb('+')
res = map(get_sign, list_of_numbers_1, list_of_numbers_2)
print(list(res))
get_sign = get_numb('*')
res = map(get_sign, list_of_numbers_1, list_of_numbers_2)
print(list(res))


"""
Задача 2: Лямбда-Функции
Использовать лямбда-функцию для реализации простой операции и 
написать такую же функцию с использованием def. 
"""

# при сохранении лямбда превращается в обычную функцию
# поэтому закомментирую
# res_1 = lambda x: x**2
# print(res_1(2))


def res_2(x):
    return x**2


print(res_2(16))

"""
Задача 3: Вызываемые Объекты
Создать класс с Rect c полями a, b которые 
задаются в __init__ и методом __call__, 
который возвращает площадь прямоугольника, 
то есть a*b.
"""


class Rect():
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __call__(self):
        return self.a*self.b


figure = Rect(24, 2)
print(figure())
