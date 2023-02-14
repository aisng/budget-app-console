from modules.budget import Budget
from modules.validators import validate_option, validate_amount

my_budget = Budget()
while True:
    user_option = input("choose operation\n1 - enter income\n2 - enter expense\n3 - show balance\n4 - show "
                        "report\n0 - exit\nyour choice: ")

    if not validate_option(user_option):
        print(f"\ninvalid operation choice '{user_option}'\nmust an integer between 0 and 4 inclusively\n")
    else:
        user_option = int(user_option)

    match user_option:
        case 1:
            user_income = input("income amount: ")
            if validate_amount(user_income):
                sender = input("sender: ")
                info = input("additional info: ")
                my_budget.add_income(user_income, sender, info)
                print(f"\namount of ${round(float(user_income), 2):.2f} has been added as 'income'\n")
            else:
                print(f"\nincorrect income amount '${user_income}'\n")
        case 2:
            user_expense = input("expense amount: ")
            if validate_amount(user_expense):
                paid_with = input("payment type: ")
                spent_on = input("commodity acquired: ")
                my_budget.add_expense(user_expense, paid_with, spent_on)
                print(f"\namount of ${round(float(user_expense), 2):.2f} has been added as 'expense'\n")
            else:
                print(f"\nincorrect expense amount '${user_expense}'\n")
        case 3:
            balance = my_budget.get_balance()
            print(f"\ncurrent balance: ${balance}", end="")
            print()
        case 4:
            print(f"\n{' budget report ':=^80}")
            print(f"{' income ':_^80}")
            print(f"{'no.':<8}{'amount':<15}{'sender':<30}{'additional info':<40}")
            print()
            print(my_budget.get_report()[0])
            print(f"{' expenses ':_^80}")
            print(f"{'no.':<8}{'amount':<15}{'payment type':<30}{'commodity acquired':<40}")
            print()
            print(my_budget.get_report()[1])
        case 0:
            print("\ngoodbye")
            break
