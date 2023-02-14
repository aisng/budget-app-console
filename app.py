from modules.budget import Budget

my_budget = Budget()
while True:
    try:
        user_input = int(input("Pasirinkite veiksmą:\n1. Įvesti pajamas\n2. Įvesti išlaidas\n3. Parodyti įvestas "
                               "pajamas ir išlaidas\n4. Parodyti pajamų ir išlaidų balansą\n5. Išeiti\nVeiksmas: "))
        match user_input:
            case 1:
                amount = float(input("\nĮveskite sumą: "))
                sender = input("Įveskite siuntėją: ")
                additional_info = input("Įveskite papildomą informaciją: ")
                my_budget.add_income_to_journal(amount, sender, additional_info)

            case 2:
                amount = float(input("\nĮveskite sumą: "))
                commodity = input("Įveskite prekę: ")
                payment_type = input("Įveskite mokėjimo tipą: ")
                my_budget.add_expenses_to_journal(amount, commodity, payment_type)
            case 3:
                print("\nPajamų ir išlaidų istorija.")
                print(f"{' Pajamos: ':*^60}\n{'Nr.':<10}{'Suma':<15}{'Siuntėjas':<20}{'Papildoma info':<20}\n",
                      my_budget.get_history()[0])
                print(f"{' Išlaidos: ':*^60}\n{'Nr.':<10}{'Suma':<15}{'Prekė':<20}{'Atsiskaitymo būdas':<20}\n",
                      my_budget.get_history()[1])
            case 4:
                print("\nBalansas:", my_budget.get_balance())
            case 5:
                print("\nIki pasimatymo.")
                break
    except ValueError:
        print("\nNeteisingas pasirinkimas.\n")
