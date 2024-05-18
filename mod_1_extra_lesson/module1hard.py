grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [
    4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sort_names = [i for i in students]
sort_names.sort()

average_rating = []
for i in grades:
    average_rating.append(sum(i)/len(i))

answer = {}
x = 0
for i in range(x, len(sort_names)):
    answer.update({sort_names[x]: average_rating[x]})
    x += 1

print("Средние баллы:", answer)
