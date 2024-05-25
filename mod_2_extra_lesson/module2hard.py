"""
Задание "Слишком древний шифр"
Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли 
вы попали в ловушку местному племени (да-да, классика "Индиана Джонса").
К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) 
с двумя каменными вставками для чисел.
В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, 
а второе было всегда пустым.

К вашему счастью рядом находился попирус, 
где были написаны правила для решения этого "ребуса".

Во вторую вставку нужно было написать те пары чисел друг за другом, 
чтобы число из первой вставки было кратно сумме их значений.
"""


import random

first_stone = random.randint(3, 20)
lst_of_first_stone = [i for i in range(1, first_stone)]


def found_all_numbers(lst):
    answer = []
    for i in range(0, len(lst)):
        for j in range(0, len(lst)):
            if first_stone % (lst[i]+lst[j]) == 0:
                answer.append([lst[i], lst[j]])
    return answer


def delete_same_elements(lst):
    result = []
    for i in lst:
        if i[::-1] not in result and i[0] != i[1]:
            result.append(i)
    return result


def print_result(first_stone, two_stone):
    print("Число n:", first_stone)
    print("Результат:")
    for i in two_stone:
        print(*i)


answer_lst = found_all_numbers(lst_of_first_stone)
result = delete_same_elements(answer_lst)
print_result(first_stone, result)
