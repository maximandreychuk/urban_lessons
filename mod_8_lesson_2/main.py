"""
Представлена функция set_password(), которая принимает пароль(str).
Проверяет, что этот пароль имеет хотя бы одну букву либо одно число.
И в зависимости от этого вызывает одно из двух исключения: если все буквы - OnlyStringLine,
если все числа - OnlyNumbersLine.
Если все ок - пароль валиден.
"""


class OnlyStringLine(Exception):
    pass


class OnlyNumbersLine(Exception):
    pass


def set_password(qwerty):
    int_to_str_lst = [str(i) for i in range(0, 10)]
    res = []
    for i in qwerty:
        if i in int_to_str_lst:
            res.append(1)
    try:
        if len(res)-len(qwerty) == 0:
            raise OnlyNumbersLine
        elif len(res) == 0:
            raise OnlyStringLine
    except OnlyNumbersLine:
        return f"Должна быть хотя бы одна буква"
    except OnlyStringLine:
        return f"Должно быть хотя бы одно число"
    else:
        return "Пароль валиден"


print(set_password("1234567"))
print(set_password("founding"))
print(set_password("123fGOo4edv"))
