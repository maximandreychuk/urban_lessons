def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print(f"<Функция {print_params.__name__} с параметрами по умолчанию>")
print_params(2, 'change stroke')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [8, 1.43, 'fooood']
values_dict = {
    'a': 2,
    'b': 'акkорд',
    'c': False
}
print("<Распаковка параметров>")
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [78, "bumble"]
print("<Распаковка + отдельные параметры>")
print_params(values_list_2, 42)
