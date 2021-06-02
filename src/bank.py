from service import Service


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

    def create_account(self, employee, customer, service):
        if customer in self.customers:
            print(f'Already Has account | bank: {self.id}')
            return False
        self.stock += service.cash
        self.customers.append(customer)
        customer.add_account(service.cash, self, employee)
        return True

    def customer_account(self, customer):
        for account in customer.accounts:
            if account.bank == self:
                return account
        return customer.accounts[0]

    def withdraw(self, employee, customer, service):
        if customer in self.customers:
            if customer.get_stock(self) >= service.cash:
                customer.add_cash(service.cash)
                account = self.customer_account(customer)
                account.stock -= service.cash
                self.stock -= service.cash
                print(f"{customer.name} get {service.cash}")
                return True
            else:
                print(f"Not enough money | bank: {self.id}")
        else:
            print(f"no account found | bank: {self.id}")
            print(f"add new service type: CREATE_ACCOUNT | bank: {self.id}")
            customer.services.append(service)
            customer.services.append(
                Service(
                    kind='CREATE_ACCOUNT',
                    seconds=1,
                    cash=service.cash,
                    bank=self
                ))
            return True

        return False

    def deposit(self, employee, customer, service):
        if customer in self.customers:
            customer.cash -= service.cash
            service.to.cash += service.cash
            account = self.customer_account(service.to)
            account.stock += service.cash
            account.bank.stock += service.cash
            print(f"{customer.name} deposit {service.cash} to {service.to.name} "
                  f"| from bank: {self.id} to bank: {account.bank.id}")
            return True
        else:
            print(f"no account found | bank: {self.id}")
        return False

    def service(self, service, customer, employee=None):
        result = False
        if service.type == 'DEPOSIT':
            result = self.deposit(employee, customer, service)
        elif service.type == 'WITHDRAW':
            result = self.withdraw(employee, customer, service)
        elif service.type == 'CREATE_ACCOUNT':
            result = self.create_account(employee, customer, service)
        return result
