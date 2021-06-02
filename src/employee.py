import random
from queue import Queue
import time


class Employee(Queue):
    def __init__(self, unique_id, name, bank):
        self.id = unique_id
        self.name = name
        code = str(random.randrange(1, 231))
        self.color = u"\u001b[38;5;" + code + "m " + code.ljust(4)
        self.bank = bank
        bank.employees.append(self)
        Queue.__init__(self)

    def add_customer(self, customer):
        self.queue.append(customer)

    def do_work(self):
        is_bank_closed = time.time() - self.bank.start_time >= self.bank.end_time
        print(f'{self.color}*****--------- start queue | Employee: {self.name}, id: {self.id} from bank: {self.bank.id} ---------*****')
        while self.queue:
            if is_bank_closed:
                print(f'work time is ended - bank: {self.bank.id} | massage from employee: {self.name}')
                break
            if self.bank.stop:
                print(f'{self.bank.boss.name}(Boss) Closed The Bank-{self.bank.id} | massage from employee: {self.name}')
                break
            customer = self.queue.pop()
            seconds = 0
            while customer.services:
                is_bank_closed = time.time() - self.bank.start_time >= self.bank.end_time
                if is_bank_closed:
                    print(f'work time is ended - bank: {self.bank.id} | massage from employee: {self.name}')
                    break
                if self.bank.stop:
                    break
                service = customer.services.pop()
                seconds += service.seconds
                print(f'{self.color}{customer.name} : {service.type} - time left : {seconds} | bank: {service.bank.id}')
                if seconds > 3:
                    seconds -= 3
                    service.seconds -= 3
                    time.sleep(3)
                    print(
                        f'{self.color}customer {customer.name} Moved to the end of the queue | bank: {service.bank.id}\n')
                    customer.services.append(service)
                    self.queue.insert(0, customer)
                    break
                else:
                    time.sleep(service.seconds)
                    seconds -= service.seconds
                    result = service.bank.service(service, customer, self)
                    if result:
                        print(
                            f'{self.color}customer {customer.name} {service.type} Done Successfully | bank: {service.bank.id}')
                    else:
                        print(f'{self.color}customer {customer.name} {service.type} Failed | bank: {service.bank.id}')
                        print(
                            f'{self.color}customer {customer.name} Moved to the end of the queue | bank: {service.bank.id}')
                        self.queue.insert(0, customer)
                        break
            print(f'{self.color}*****--------- end queue | Employee: {self.name}, id: {self.id} from bank: {self.bank.id} ---------*****')
