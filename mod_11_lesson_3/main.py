"""
Необходимо создать функцию, 
которая принимает объект (любого типа) в качестве аргумента 
и проводит интроспекцию этого объекта, чтобы определить его тип, 
атрибуты, методы, модуль, и другие свойства.
"""


import inspect


def introspection_info(obj):
    res = {}
    res['Tип объекта'] = type(obj)
    res['Атрибуты объекта'] = [i for i in dir(obj) if i.startswith('__')]
    res['Методы объекта'] = [i for i in dir(obj) if not i.startswith('__')]
    res['Модуль, к которому объект принадлежит'] = inspect.getmodule(obj)
    try:
        iter(obj)
        res['Итерируемый ли объект ?'] = True
    except TypeError:
        res['Итерируемый ли объект ?'] = False
    return res


print(introspection_info([23]))
