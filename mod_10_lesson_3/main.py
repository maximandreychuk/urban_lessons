"""
Реализуйте программу, которая имитирует доступ к общему ресурсу 
с использованием механизма блокировки потоков.

Класс BankAccount должен отражать банковский счет с балансом и методами 
для пополнения и снятия денег. Необходимо использовать механизм блокировки, 
чтобы избежать проблемы гонок (race conditions) при модификации общего ресурса.
"""

import threading
import random


class BankAccount(threading.Thread):
    def __init__(self, account, operations, lock, *args, **kwargs):
        super(BankAccount, self).__init__(*args, **kwargs)
        self.account = account
        self.balance = 1000
        self.operations = operations
        self.operation_lock = lock

    def deposit(self, money):
        self.balance += money
        # return print(f"{self.account}, вы внесли {money}, ваш депозит {self.balance}")

    def withdrawal(self, money):
        self.balance -= money
        # if (self.balance - money) < 0:
        #     self.balance += money
        #     raise print(
        #         f"{self.account}, вы можете снять максимум {self.balance}")
        # else:
        #     return print(f"{self.account}, вы сняли {money}, ваш депозит {self.balance}")

    def run(self):
        for day in range(self.operations):
            with self.operation_lock:
                self.deposit(45)
                self.withdrawal(33)

    def __str__(self):
        return f"\n {self.account} - {self.balance} \n"


lock = threading.Lock()
friend_1 = BankAccount("Том", operations=100000, lock=lock)
friend_2 = BankAccount("Джери", operations=100000, lock=lock)

friend_1.start()
friend_2.start()


friend_1.join()
friend_2.join()

print(friend_1, friend_2)
