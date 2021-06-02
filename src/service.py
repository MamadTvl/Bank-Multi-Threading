class Service:
    def __init__(self, kind, seconds, cash=None, bank=None, to=None):
        self.type = kind
        self.seconds = seconds
        self.cash = cash
        self.bank = bank
        self.to = to
