"""
Моделирование программы для управления данными о движении товаров на складе 
и эффективной обработки запросов на обновление информации в многопользовательской среде.

Представим, что у вас есть система управления складом, 
где каждую минуту поступают запросы на обновление информации 
о поступлении товаров и отгрузке товаров.
Наша задача заключается в разработке программы, 
которая будет эффективно обрабатывать эти запросы в многопользовательской среде, 
с использованием механизма мультипроцессорности для 
обеспечения быстрой реакции на поступающие данные.
"""


from requests_fold import requests
from multiprocessing import Manager, Process


class WarehouseManager(Process):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = Manager().dict()

    def process_request(self, request):
        if request[1] == "receipt":
            if request[0] in self.data.keys():
                self.data[request[0]] += request[2]
            else:
                self.data[request[0]] = request[2]
        elif request[1] == "shipment":
            if request[0] in self.data.keys() and self.data[request[0]] >= request[2]:
                self.data[request[0]] -= request[2]

    def run(self, requests):
        for req in requests:
            process = Process(target=self.process_request, args=(req,))
            process.start()
            process.join()

    def __str__(self):
        return f"{self.data}"


if __name__ == '__main__':
    manager = WarehouseManager()
    manager.run(requests)
    print(manager)
