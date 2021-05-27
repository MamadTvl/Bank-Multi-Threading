class boss:
    def __init__(self, unique_id, name, bank):
        self.id = unique_id
        self.name = name
        self.bank = bank

    def end_of_working_hour(self):
        self.bank.stop = True
