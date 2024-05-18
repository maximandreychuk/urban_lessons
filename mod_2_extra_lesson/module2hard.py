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
