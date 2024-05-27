from math import sqrt


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
