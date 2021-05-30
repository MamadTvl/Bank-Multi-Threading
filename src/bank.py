def customer_account(customer):
    for account in customer.accounts:
        if account.Bank == Bank:
            return account


class Bank:
    def __init__(self, unique_id, boss, employees, customers, stock, start_time, end_time, stop=False):
        self.boss = boss
        self.employees = employees
        self.customers = customers
        self.id = unique_id
        self.stock = stock
        self.start_time = start_time
        self.end_time = end_time
        self.stop = stop

    def create_account(self, employee, customer, cash):
        self.stock += cash
        self.customers.append(customer)
        customer.add_account(cash, Bank, employee)
        return True

    def withdraw(self, customer, cash):
        if customer in self.customers:
            if customer.get_stock(Bank) >= cash:
                customer.add_cash(cash)
                customer_account(customer).stock -= cash
                self.stock -= cash
                print("%s get %s" % customer.name % cash)
                return True
            else:
                print("Not enough money ")
        else:
            print("no account found")
        return False

    def deposit(self, customer, cash):
        if customer in self.customers:
            customer.cash += cash
            customer_account(customer).stock += cash
            self.stock += cash
            print("%s add %s" % customer.name % cash)
            return True
        else:
            print("no account found")
        return False

    def service(self, service, customer, employee=None):
        if service.type == 'DEPOSIT':
            self.deposit(customer, service.cash)
        elif service.type == 'WITHDRAW':
            self.withdraw(customer, service.cash)
        elif service.type == 'CREATE_ACCOUNT':
            self.create_account(employee, customer, service.cash)
