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
