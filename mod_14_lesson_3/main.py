"""
Как мы все знаем айтишники любят путешествовать, а география студентов Urban'а очень большая.
Все они были в разных городах и странах, но посетить осталось ещё не мало. 
Выпускники уже  планируют, куда поедут после окончания курсов отдохнуть.
Нужно помочь им определить, кто в каких городах был и в какие города они хотят поехать. 
Определите, какие города можно выбрать для путешествия, при условии, 
что никто из потока в них никогда не был.

Напишите функцию write_holiday_cities(first_letter), которая:
Принимает параметром первую букву имени человека - first_letter.
Функция должна:
Получить данные из travel_notes.csv и записать в holiday.csv:
В каких городах студенты с именем на first_letter уже были.
Какие города студенты с именем на first_letter хотят посетить.
В каких городах студенты с именем на first_letter ещё не были.
Какой первый город эти студенты посетят (в алфавитном порядке).

Для начала установите виртуальное окружение и зависимости:
python3 -m venv venv   
source venv/bin/activate
pip3 install -r requirements.txt
"""


import csv


def write_holiday_cities(first_letter):
    with open('travel-notes.csv', 'r', newline='', encoding='utf-8') as csv_file:
        lst = []
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            lst.append(row)

    with open('holiday.csv', 'w', newline='') as out_csv:
        visited = []
        want_to_visit = []
        for el in lst:
            if str(el[0]).startswith(first_letter):
                visited.append(el[1])
                want_to_visit.append(el[2])
        visited = [i.split(';') for i in visited]
        want_to_visit = [i.split(';') for i in want_to_visit]

        mod_visited = []
        mod_want_to_visit = []
        for cities in visited:
            for index in range(len(cities)):
                if not cities[index] in mod_visited:
                    mod_visited.append(cities[index])
        for cities in want_to_visit:
            for index in range(len(cities)):
                if not cities[index] in mod_want_to_visit:
                    mod_want_to_visit.append(cities[index])
        try:
            res_visited, res_want_to_visit = sorted(
                mod_visited), sorted(mod_want_to_visit)
            res_visited = ['Посетили: '] + res_visited
            never_been = ['Никогда не были в: '] + res_want_to_visit

            next_city = ['Следующим городом будет: '] + [res_want_to_visit[0]]
            res_want_to_visit = ['Хотят посетить: '] + res_want_to_visit
            writer = csv.writer(out_csv)
            writer.writerow(res_visited)
            writer.writerow(res_want_to_visit)
            writer.writerow(never_been)
            writer.writerow(next_city)
        except IndexError:
            print('Имён на такую букву нет')


get_letter = input("Ввод: ")
write_holiday_cities(get_letter)
