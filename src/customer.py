from datetime import datetime

from account import account


class customer:
    def __init__(self, unique_id, cash, name, accounts):
        self.id = unique_id
        self.cash = cash
        self.name = name
        self.accounts = accounts

    def add_account(self, cash, bank, employee):
        self.cash -= cash
        self.accounts.append(account(bank, customer, cash, employee, datetime))

    def get_stock(self, bank):
        for acc in self.accounts:
            if acc.bank == bank:
                return acc.stock

    def add_cash(self, cash):
        self.cash += cash
