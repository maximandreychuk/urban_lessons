def test(*args):
    print(*args)


test(4, 'd', ['332'], {3: 3})


def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)


print(f'Факториaл числа: {factorial(33)}')
