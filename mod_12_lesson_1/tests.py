"""
Urban решил устроить соревнования между студентами по бегу, 
ибо сидячий образ жизни ни к чему хорошему не приведёт.
Некоторые участники упорно готовились к нему, 
а некоторые даже вебинары не посещали по пройденным модулям. 
Вот и получилось, что некоторые на соревнованиях бегали и выигрывали, 
а кто просто ходил по дистанции, те проигрывали.
"""


import unittest
from HumanMoveTest.main import Student


class MyTest(unittest.TestCase):
    def setUp(self):
        self.john = Student('John')
        self.garry = Student('Garry')

    def test_walk(self):
        for _ in range(1, 11):
            self.john.walk()
        self.assertEqual(self.john.distance, 50, "Дистанции не равны")

    def test_run(self):
        for _ in range(1, 11):
            self.john.run()
        self.assertEqual(self.john.distance, 100, "Дистанции не равны")

    def test_who_is_faster(self):
        for _ in range(1, 11):
            self.john.walk()
        for _ in range(1, 11):
            self.garry.run()
        self.assertGreater(
            self.garry.distance,
            self.john.distance,
            f"{self.garry} должен преодолеть дистанцию больше, чем {self.john}.")


if __name__ == "__main__":
    unittest.main()
