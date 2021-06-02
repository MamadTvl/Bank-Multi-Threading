import random

from bank import Bank
from boss import Boss
from customer import Customer
from employee import Employee
from service import Service
import threading


def set_service(index):
    if index == 0:
        return {'kind': 'CREATE_ACCOUNT', 'seconds': 1, 'cash': 2000}
    elif index == 1:
        return {'kind': 'DEPOSIT', 'seconds': 5, 'cash': 1000, 'to': None}
    elif index == 2:
        return {'kind': 'WITHDRAW', 'seconds': 3, 'cash': 500}


def create_service_data(kind, seconds, cash, bank):
    return Service(kind, seconds, cash, bank)


def create_bank_data(unique_id, boss, employees, customers, stock, start_time, end_time, stop):
    return Bank(unique_id, boss, employees, customers, stock, start_time, end_time, stop)


def create_employee_data(unique_id, name, bank):
    return Employee(unique_id, name, bank)


def create_boss_data(unique_id, name, bank):
    return Boss(unique_id, name, bank)


def create_customer_data(unique_id, cash, name, accounts, services):
    return Customer(unique_id, cash, name, accounts, services)


# 4 bank, 4 boss, each bank has 4 employees and 4 customers,
# 4 customer -> 2 of them want to create_account
# 2 other want to DEPOSIT but has no account so moved to the end of queue

"""initial values"""

banks = []
for i in range(4):
    banks.append(
        create_bank_data(
            unique_id=i,
            boss=None,
            employees=[],
            customers=[],
            stock=0,
            start_time=8,
            end_time=16,
            stop=False,
        )
    )
bosses = []
for i in range(4):
    bosses.append(
        create_boss_data(
            unique_id=i,
            bank=banks[i],
            name=f'Mr. {i}'
        )
    )

employees = []
employee_id = 10001
for bank in banks:
    for i in range(4):
        employees.append(
            create_employee_data(
                unique_id=employee_id,
                bank=bank,
                name=f'Mr. {employee_id}'
            )
        )
        employee_id += 1

services = []
for i in range(4):
    for j in range(3):
        service_details = set_service(j)
        services.append(
            create_service_data(
                bank=banks[i],
                seconds=service_details['seconds'],
                kind=service_details['kind'],
                cash=service_details['cash'],
            )
        )

customer_id = 43100
customers = []
for i in range(16):
    customers.append(
        create_customer_data(
            unique_id=customer_id,
            cash=10000,
            name=f'Mr. {customer_id}',
            services=[],
            accounts=[],
        )
    )
    customer_id += 1

for customer in customers:
    for service in services:
        if service.type == 'DEPOSIT':
            rand_index = 0
            while True:
                rand_index = random.randrange(0, 16)
                if customers[rand_index] != customer:
                    break
            service.to = customers[rand_index]
        customer.add_service(service)

for i in range(16):
    employees[i].add_customer(customers[i])

threads = []

for employee in employees:
    thread = threading.Thread(target=employee.do_work)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

