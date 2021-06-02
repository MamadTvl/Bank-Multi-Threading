import time
import random
from queue import Queue


class Employee(Queue):
    def __init__(self, unique_id, name, bank):
        self.id = unique_id
        self.name = name
        code = str(random.randrange(1, 231))
        self.color = u"\u001b[38;5;" + code + "m " + code.ljust(4)
        bank.employees.append(self)
        Queue.__init__(self)

    def add_customer(self, customer):
        self.queue.append(customer)

    def do_work(self):
        print(f'{self.color}*****--------- start queue | Employee: {self.name}, id: {self.id} ---------*****')
        while self.queue:
            customer = self.queue.pop()
            seconds = 0
            while customer.services:
                service = customer.services.pop()
                seconds += service.seconds
                print(f'{self.color}{customer.name} : {service.type} - time left : {seconds} | bank: {service.bank.id}')
                if seconds > 3:
                    seconds -= 3
                    service.seconds -= 3
                    time.sleep(3)
                    print(f'{self.color}customer {customer.name} Moved to the end of the queue | bank: {service.bank.id}\n')
                    customer.services.append(service)
                    self.queue.insert(0, customer)
                    break
                else:
                    time.sleep(service.seconds)
                    seconds -= service.seconds
                    result = service.bank.service(service, customer, self)
                    if result:
                        print(f'{self.color}customer {customer.name} {service.type} Done Successfully | bank: {service.bank.id}')
                    else:
                        print(f'{self.color}customer {customer.name} {service.type} Failed | bank: {service.bank.id}')
                        print(f'{self.color}customer {customer.name} Moved to the end of the queue | bank: {service.bank.id}')
                        self.queue.insert(0, customer)
                        break
            print(f'{self.color}*****--------- end queue | Employee: {self.name}, id: {self.id} ---------*****')
