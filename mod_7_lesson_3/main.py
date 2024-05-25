print("- - - использование % - - - ")
team1_num = 5
print("В команде Мастера кода участников: %s!" % (team1_num))
team1_num, team2_num = 5, 6
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))


print("- - - использование format() - - - ")
score_2, team1_time = 42, 18015.2
print("Команда Волшебники данных решила задач: {}!".format(score_2))
print("Волшебники данных решили задачи за {} с !".format(team1_time))


print("- - - использование f-строк - - - ")
score_1, score_2 = 40, 42
print(f"Команды решили {score_1} и {score_2} задач.")
challenge_result = "победа команды Мастера кода!"
print(f"Результат битвы: {challenge_result}")
tasks_total, time_avg = 82, 350.4
print(
    f"Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")
