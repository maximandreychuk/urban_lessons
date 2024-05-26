"""
Дан список целых чисел, примените функции map и filter так,
чтобы в конечном списке оставить нечётные квадраты чисел.
"""
lst = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]


def qvadrat(i):
    return i**2


def delenie(i):
    return i % 2


res = map(qvadrat, filter(delenie, lst))
print(list(res))
