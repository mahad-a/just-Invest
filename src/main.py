import bcrypt
from checkers import *
import getpass

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


def encrypt_password(password: str):
    password_byte = password.encode("utf-8") # encode password in bytes
    hash_result = bcrypt.hashpw(password_byte, bcrypt.gensalt(rounds=10)) # hash the password and add salt
    if bcrypt.checkpw(password_byte, hash_result):
        return hash_result

def sign_up():
    # while True:
    print("-"*50, "\nSign up: ")
    name = input("Enter your name: ")
    for available_roles in MENU_AND_ROLE.keys():
        print(f"- {available_roles}")
    role = input("Enter your role: ")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password (Hidden for security): ")

    if is_password_valid(username, password) and is_role_valid(role):
        hashed_password = encrypt_password(password)
        with open(PASSWORDS, 'a') as password_file:
            password_file.write("Name: %s, Username: %s, Role: %s, Password: %s\n" % (name.title(), username, role.title(), hashed_password.decode("utf-8")))
            justInvestMenu(role.title())
            # break
    else:
        print("One of the inputted values were not a valid input.")

def log_in():
    print("-"*50, "\nLog in: ")    
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password (Hidden for security): ")
    with open(PASSWORDS, "r") as file:
        for line in file:
            stored_name, stored_username,stored_role, stored_password_hash = line.strip().split(",")

            if username == stored_username:
                if bcrypt.checkpw(password.encode("utf-8"), stored_password_hash.encode("utf-8")):
                    print("ACCESS GRANTED!\nLogin successful! Welcome %s" % stored_name)
                    justInvestMenu(stored_role)
                    return
                else:
                    print("ACCESS DENIED!\nIncorrect password.")
    print("Username not found.")
    return

def main_menu():
    print("-" * 50, "\nMain Menu")
    while True:
        print("1. Sign up \n2. Log in ")
        choice = input("Enter your choice (1, 2): ")

        if choice == "1":
            sign_up()
            break
        elif choice == "2":
            log_in()
            break
        else:
            print("Invalid Input, try again. ")

if __name__ == "__main__":
    justInvestMenu("Client")
    # main_menu()
        