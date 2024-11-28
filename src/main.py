from Problem3 import * 
from Problem4 import * 
def main_menu():
    print("-" * 50, "\nMain Menu")
    while True:
        print("1. Sign up \n2. Log in \n3. Quit")
        choice = input("Enter your choice (1, 2, 3): ")

        if choice == "1":
            sign_up()
            break
        elif choice == "2":
            log_in()
            break
        elif choice == "3":
            print("Ending program... Goodbye")
            exit()
        else:
            print("Invalid Input, try again. ")

if __name__ == "__main__":
    # justInvestMenu("Client")
    main_menu()
        