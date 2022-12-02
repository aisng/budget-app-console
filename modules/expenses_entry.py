from modules.entry import Entry


class ExpensesEntry(Entry):
    def __init__(self, amount, commodity, payment_type):
        super().__init__(amount)
        self.commodity = commodity
        self.payment_type = payment_type
