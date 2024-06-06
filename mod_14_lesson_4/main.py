"""
Напишите функцию employees_rewrite(sort_type), которая:
Принимает параметром тип сортировки (ключ) - sort_type.

Функция должна:
Получить данные из employees.json и записать в employees_[sort_type]_sorted.json:
Формат записи должен быть как в исходном файле.
Если сортировка производится по строковым значения, то в алфавитном порядке.
Если сортировка производится по числовым значениям, то в порядке убывания.

"""


import json


def employees_rewrite(sort_type):
    with open('employees.json', 'r') as read:
        file = json.load(read).get('employees')

    if sort_type.upper() == 'FIRSTNAME':
        with open('employees_firstname_sorted.json', 'w') as res:
            sor = sorted(file, key=lambda x: x['firstName'])
            res.write(json.dumps(sor, indent=4))

    elif sort_type.upper() == 'LASTNAME':
        with open('employees_lastname_sorted.json', 'w') as res:
            sor = sorted(file, key=lambda x: x['lastName'])
            res.write(json.dumps(sor, indent=4))

    elif sort_type.upper() == 'DEPARTMENT':
        with open('employees_department_sorted.json', 'w') as res:
            sor = sorted(file, key=lambda x: x['department'])
            res.write(json.dumps(sor, indent=4))

    elif sort_type.upper() == 'SALARY':
        with open('employees_salary_sorted.json', 'w') as res:
            sor = sorted(file, key=lambda x: x['salary'])[::-1]
            res.write(json.dumps(sor, indent=4))
    else:
        raise ValueError(f'Bad key "{sort_type}" for sorting')


employees_rewrite('firstNamE')
employees_rewrite('lastnAmE')
employees_rewrite('DEPartment')
employees_rewrite('saLAry')
employees_rewrite('saL;Ary')
