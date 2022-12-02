from modules.entry import Entry


class IncomeEntry(Entry):
    def __init__(self, amount, sender, additional_info):
        super().__init__(amount)
        self.sender = sender
        self.additional_info = additional_info

    def __str__(self):
        return f"Suma: {self.amount}, siuntėjas: {self.sender}, papildoma informacija: {self.additional_info}"
