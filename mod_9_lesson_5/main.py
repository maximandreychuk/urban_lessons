"""
Задание:
Напишите 2 функции:
Функция которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", 
если результат 1ой функции будет простым числом и "Составное" в противном случае.
"""


def is_prime(func):
    def wrapper(a, b, c):
        res = func(a, b, c)
        for i in range(2, res//2 + 1):
            if res % i == 0:
                return f'Составное {res}'
        return f'Простое {res}'
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a+b+c


print(sum_three(0, 0, 38))
