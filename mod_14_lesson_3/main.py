import csv
import pandas as pandasForSortingCSV


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
