from modules.entry import Entry


class EntryOfExpense(Entry):
    def __init__(self, amount, commodity, payment_type):
        super().__init__(amount)
        self.commodity = commodity
        self.payment_type = payment_type

    def __repr__(self):
        return f"{self.amount}_{self.payment_type}_{self.commodity}"