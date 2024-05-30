import queue
import threading
import time
from queue import Queue


class Table():
    def __init__(self, number: int, is_busy: bool = False):
        self.number = number
        self.is_busy = is_busy


class Customer():
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number


class Cafe(threading.Thread):
    def __init__(self, tables: list[Table], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queue_customers = queue.Queue(maxsize=20)
        self.tables = tables

    def customer_arrival(self):
        for numb in range(1, 21):
            customer = Customer(number=numb)
            self.queue_customers.put(customer)
            time.sleep(1)
            print(f"Посетитель номер {customer.number} прибыл")

    def serve_customer(self):
        pass


table_1 = Table(1)
table_2 = Table(2)
table_3 = Table(3)
tables = [table_1, table_2, table_3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()
