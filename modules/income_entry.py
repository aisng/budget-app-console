from modules.entry import Entry


class EntryOfIncome(Entry):
    def __init__(self, amount, sender, additional_info):
        super().__init__(amount)
        self.sender = sender
        self.additional_info = additional_info

    def __repr__(self):
        return f"{self.amount}_{self.sender}_{self.additional_info}"
