class Boss:
    def __init__(self, unique_id, name, bank):
        self.id = unique_id
        self.name = name
        self.bank = bank
        bank.boss = self

    def end_of_working_hour(self):
        self.bank.stop = True
