import customtkinter as ctk
from modules.budget import Budget
from modules.validators import validate_option, validate_amount

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("400x500")
root.resizable(False, False)
root.title("My Budget")

entries_frame = ctk.CTkFrame(master=root, width=350, height=215)
balance_frame = ctk.CTkFrame(master=root, width=350, height=215)
entries_frame.grid(row=0, column=0, padx=25, pady=(25, 10), sticky='NSEW')
balance_frame.grid(row=1, column=0, padx=25, pady=(10, 25), sticky='NSEW')

# entries_frame.pack(expand=True, fill=ctk.BOTH, padx=16, pady=(16, 8))
# balance_frame.pack(expand=True, fill=ctk.BOTH, padx=16, pady=(8, 16))

# variables

amount_entry = ctk.StringVar()

# entries frame

user_amount = ctk.CTkEntry(master=entries_frame, placeholder_text="Enter your income")
btn_submit = ctk.CTkButton(master=entries_frame, text="Submit")
type_label = ctk.CTkLabel(master=entries_frame, text="Choose type:")

type_income_rb = ctk.CTkRadioButton(master=entries_frame, variable=amount_entry, text="Income")
type_expense_rb = ctk.CTkRadioButton(master=entries_frame, variable=amount_entry, text="Expense")

type_label.grid(column=3, row=0, sticky='NSEW')
type_income_rb.grid(column=3, row=1, sticky='NSEW')
type_expense_rb.grid(column=3, row=2, sticky='NSEW')

user_amount.grid(column=1, row=2, columnspan=2, sticky='NSEW')
btn_submit.grid(column=1, row=4, columnspan=3, sticky='NSEW')

#
#

#
# # pakcking entries to entries frame
#
# type_label.grid(row=0, column=3)
# user_amount.grid(row=2, column=0, rowspan=2, sticky=ctk.E)
# btn_submit.grid(row=4, column=0, rowspan=2, sticky=ctk.E)
#
# select_type_income.grid(row=2, column=3)
# select_type_expense.grid(row=3, column=3)

# entries_frame.columnconfigure(0, weight=1)
# entries_frame.columnconfigure(1, weight=2)

root.mainloop()
