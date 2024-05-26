"""
Напишите функцию-генератор all_variants, 
которая будет возвращать все подпоследовательности переданной строки. 
В функцию передаётся только сама строка.
"""


def all_variants(text):
    for start in range(0, len(text)):
        for end in range(start+1, len(text)+1):
            yield text[start:end]


for s in all_variants('abc'):
    print(s)
