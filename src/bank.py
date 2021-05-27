class bank:
    def __init__(self, unique_id, boss, employees, customers, stock, start_time, end_time, stop=False):
        self.boss = boss
        self.employees = employees
        self.customers = customers
        self.customers_count = len(customers)
        self.id = unique_id
        self.stock = stock
        self.start_time = start_time
        self.end_time = end_time
        self.stop = stop

    def create_account(self, employee, customer, cash):
        self.stock += cash
        self.customers.append(customer)
        customer.add_account(cash, bank, employee)

    def customer_account(self, customer):
        for account in customer.accounts:
            if account.bank == bank:
                return account

    def get_cash(self, customer, cash):
        if customer in self.customers:
            if customer.get_stock(bank) >= cash:
                customer.add_cash(cash)
                self.customer_account(customer).stock -= cash

                print("%s get %s" % customer.name % cash)
