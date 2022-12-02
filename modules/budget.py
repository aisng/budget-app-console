import pickle
from modules.expenses_entry import ExpensesEntry
from modules.income_entry import IncomeEntry


class Budget:
    def __init__(self):
        self.journal = self.read_from_pickle()

    def read_from_pickle(self):
        try:
            with open("budget.pkl", "rb") as r_file:
                budget_file = pickle.load(r_file)
        except FileNotFoundError:
            budget_file = []
        return budget_file

    def add_to_pickle(self, data_in):
        with open("budget.pkl", "wb") as w_file:
            pickle.dump(data_in, w_file)


    def add_income_to_journal(self, amount, sender, additional_info):
        income_entry = IncomeEntry(amount, sender, additional_info)
        self.journal.append(income_entry)
        self.add_to_pickle(self.journal)

    def add_expenses_to_journal(self, amount, commodity, payment_type):
        expenses_entry = ExpensesEntry(amount, commodity, payment_type)
        self.journal.append(expenses_entry)
        self.add_to_pickle(self.journal)

    def get_balance(self):
        balance = 0
        for entry in self.journal:
            if type(entry) is IncomeEntry:
                balance += entry.amount
            if type(entry) is ExpensesEntry:
                balance -= entry.amount
        return balance

    def get_history(self):
        income = str()
        expenses = str()
        for nr, item in enumerate(self.journal, 1):
            if type(item) is IncomeEntry:
                income += f"{nr : <5}{item.amount : ^15}{item.sender : ^20}{item.additional_info : ^20}\n"
            if type(item) is ExpensesEntry:
                expenses += f"{nr : <5}\t{item.amount : ^15}\t {item.commodity : ^20}\t {item.payment_type : ^20}\n"

        return [income, expenses]

