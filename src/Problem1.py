from checkers import *
from main import main_menu

def justInvestMenu(user_role):
    print("justInvest System\n", "-"*50, "\nOperations available on the system:")
    menu = list(get_access(user_role))
    menu.append("Log out")
    for idx, option in enumerate(menu, start=1):
        print(f" {idx}. {option}")
    user_input = input("Enter your option: ")
    result = process_user_selection(user_input, len(menu))

    if result:
        selection = menu[result-1]
        if selection == "Log out":
            print("Logging out...")
            main_menu()
        print("ACCESS GRANTED TO %s" % selection)