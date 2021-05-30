import time

from src.queue import Queue


class Employee(Queue):
    def __init__(self, unique_id, name):
        self.id = unique_id
        self.name = name
        Queue.__init__(self)

    def add_customer(self, customer):
        self.queue.append(customer)

    def do_work(self):
        while self.queue:
            customer = self.queue.pop()
            for service in customer.services:
                # todo: before start this make sure all services is in this bank
                print(f'{customer.name} : {service.type} ')
                if service.seconds > 3:
                    service.seconds -= 3
                    time.sleep(3)
                    self.queue.insert(0, customer)
                else:
                    time.sleep(service.seconds)
                service.account.bank.service(service, customer, self)



