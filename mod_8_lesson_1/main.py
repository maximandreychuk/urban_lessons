from typing import Union


def add_everything_up(numb: Union[str, int, float],
                      stroke: Union[str, int, float]) -> TypeError | str:
    try:
        return round(numb + stroke, 3)
    except TypeError:
        if isinstance(numb, float) or isinstance(numb, int):
            return f'{str(numb)}{stroke}'
        else:
            return f'{numb}{str(stroke)}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
