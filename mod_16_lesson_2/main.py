"""
Техническое задание:
Создайте базу данных students.db
В базе данных должны существовать 2 таблицы: students и grades
В таблице students должны присутствовать следующие поля: id, name, age
В таблице grades должны присутствовать следующие поля: id, student_id, subject, grade
Так же нужно создать класс University со следующими атрибутами и методами:
name - имя университета
add_student(name, age) - метод добавления студента.
add_grade(sudent_id, subject, grade) - метод добавления оценки.
get_students(subject=None) - метод для возврата списка студентов в формате
[(Ivan, 26, Python, 4.8), (Ilya, 24, PHP, 4.3)],где subject, 
если не является None(по умолчанию) и если такой предмет существует, 
выводит студентов только по этому предмету.
"""


import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()


# with conn:
#     conn.execute("""
#         CREATE TABLE students (
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             age INTEGER
# );
#     """)

# cursor.execute("""
#         CREATE TABLE grades (
#             id INTEGER PRIMARY KEY,
#             subject TEXT,
#             grade FLOAT,
#             student_id INTEGER,
#             FOREIGN KEY(student_id) REFERENCES students(id)
# );
#     """)


class University():
    def __init__(self, uni_name):
        self.uni_name = uni_name

    def add_student(self, name: str, age: int) -> None:
        cursor.execute(
            f'INSERT INTO students (name, age) VALUES("{name}", "{age}")')
        conn.commit()

    def add_grade(self, sudent_id: int, subject: str, grade: float) -> None:
        cursor.execute(
            f'INSERT INTO grades (student_id, subject, grade) VALUES("{sudent_id}", "{subject}", "{grade}")')
        conn.commit()

    def get_students(self, subject=None):
        if subject is None:
            cursor.execute(
                'SELECT students.name, students.age, grades.subject, grades.grade FROM students, grades WHERE grades.student_id = students.id')
            res = cursor.fetchall()
            print(res)
        else:
            cursor.execute(
                f'SELECT students.name, students.age, grades.subject, grades.grade FROM students, grades WHERE grades.student_id = students.id AND grades.subject = "{subject}"')
            res = cursor.fetchall()
            print(res)


u1 = University('Urban')
u1.get_students('Celery')
u1.get_students('MongoDB')
u1.get_students()

conn.close()
