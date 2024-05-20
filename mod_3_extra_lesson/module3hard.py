data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def str_to_numb(int_or_str):
    """
    Eсли тип переменной - строка, то считается его длина.
    """
    if isinstance(int_or_str, str):
        return len(int_or_str)
    return int_or_str


def counter(*args):
    answer = []
    for structure in args:

        if isinstance(structure, list):
            for i in structure:
                answer.append(counter(i))

        elif isinstance(structure, set):
            for i in structure:
                answer.append(counter(i))

        elif isinstance(structure, dict):
            for k, v in structure.items():
                answer.append(counter(k, v))

        elif isinstance(structure, tuple):
            for i in structure:
                answer.append(counter(i))
        else:
            answer.append(str_to_numb(structure))

    return sum(answer)


print(counter(data_structure))
