import time

from queue import Queue


class Employee(Queue):
    def __init__(self, unique_id, name, bank):
        self.id = unique_id
        self.name = name
        bank.employees.append(self)
        Queue.__init__(self)

    def add_customer(self, customer):
        self.queue.append(customer)

    def do_work(self):
        while self.queue:
            customer = self.queue.pop()
            while customer.services:
                service = customer.services.pop()
                # todo: before start this make sure all services is in this bank
                print(f'{customer.name} : {service.type} ')
                if service.seconds > 3:
                    service.seconds -= 3
                    time.sleep(3)
                    print(f'customer {customer.name} Moved to the end of the queue')
                    customer.services.append(service)
                    self.queue.insert(0, customer)
                    break
                else:
                    time.sleep(service.seconds)
                    result = service.bank.service(service, customer, self)
                    if result:
                        print('job Done Successfully')
                    else:
                        print('Failed')
                        print(f'customer {customer.name} Moved to the end of the queue')
                        self.queue.insert(0, customer)
                        break

