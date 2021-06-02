from datetime import datetime

from account import Account


class Customer:
    def __init__(self, unique_id, cash, name, accounts, services):
        self.id = unique_id
        self.cash = cash
        self.name = name
        self.accounts = accounts
        self.services = services

    def add_service(self, service):
        self.services.append(service)

    def add_account(self, cash, bank, employee):
        self.cash -= cash
        self.accounts.append(Account(bank, self, cash, employee, datetime))

    def get_stock(self, bank):
        for acc in self.accounts:
            if acc.bank == bank:
                return acc.stock

    def add_cash(self, cash):
        self.cash += cash
