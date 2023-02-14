import pickle
import textwrap
from modules.expenses_entry import EntryOfExpense
from modules.income_entry import EntryOfIncome


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

    def save_to_pickle(self, data_in):
        with open("budget.pkl", "wb") as w_file:
            pickle.dump(data_in, w_file)

    def add_income(self, amount, sender, additional_info):
        income_entry = EntryOfIncome(amount, sender, additional_info)
        self.journal.append(income_entry)
        self.save_to_pickle(self.journal)

    def add_expense(self, amount, commodity, payment_type):
        expenses_entry = EntryOfExpense(amount, commodity, payment_type)
        self.journal.append(expenses_entry)
        self.save_to_pickle(self.journal)

    def get_balance(self):
        balance = 0
        for entry in self.journal:
            if type(entry) is EntryOfIncome:
                balance += float(entry.amount)
            if type(entry) is EntryOfExpense:
                balance -= float(entry.amount)
        return balance

    def get_report(self):
        income = str()
        expenses = str()
        for nr, item in enumerate(self.journal, 1):
            if type(item) is EntryOfIncome:
                income += f"{nr : <10}{item.amount:<15}{item.sender:<20}{item.additional_info:<20}\n"
            if type(item) is EntryOfExpense:
                expenses += f"{nr : <10}{item.amount:<15}{item.commodity:<20}{textwrap.fill(item.payment_type, 20):<20}\n"

        return [income, expenses]
