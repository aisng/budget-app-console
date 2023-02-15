import customtkinter as ctk
from modules.budget import Budget
from modules.validators import validate_option, validate_amount

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("400x500")
root.title("My Budget")

left_frame = ctk.CTkFrame(master=root)
left_frame.pack(expand=True, fill=ctk.BOTH, padx=10, pady=10)

entries_frame = ctk.CTkFrame(master=left_frame)
balance_frame = ctk.CTkFrame(master=left_frame)

entries_frame.pack(expand=True, fill=ctk.BOTH, padx=16, pady=(16, 8))
balance_frame.pack(expand=True, fill=ctk.BOTH, padx=16, pady=(8, 16))

# entries frame

income_entry = ctk.CTkEntry(master=entries_frame, placeholder_text="enter your income")
btn_submit_income = ctk.CTkButton(master=entries_frame, text="Submit", width=100)

expense_entry = ctk.CTkEntry(master=entries_frame, placeholder_text="enter your expense")
btn_submit_expense = ctk.CTkButton(master=entries_frame, text="Submit", width=100)

# pakcking entries to entries frame

income_entry.grid(row=0, column=0, padx=8, pady=8, sticky=ctk.W)
btn_submit_income.grid(row=0, column=1, padx=8, pady=8, sticky=ctk.W)

expense_entry.grid(row=1, column=0, padx=8, pady=8, sticky=ctk.W)
btn_submit_expense.grid(row=1, column=1, padx=8, pady=8, sticky=ctk.W)

entries_frame.columnconfigure(0, weight=1)
entries_frame.columnconfigure(1, weight=2)

root.mainloop()
