import getpass
from Problem1 import justInvestMenu, privileges
from Problem2 import get_account_from_file
import bcrypt

PASSWORDS = "docs/passwd.txt"

# display for access privileges handled in Problem1.py

def log_in(): # simple login user interface
    print("-"*50, "\nLog in: ")    
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password (Hidden for security): ")
    
    found_account = get_account_from_file(username, password)

    if found_account:
        stored_name, stored_role = found_account
        print("ACCESS GRANTED!\nLogin successful! Welcome %s" % stored_name)
        privileges(username, stored_role)
        justInvestMenu(stored_role) # display options based on user's role
    else:
        print("ACCESS DENIED!\nIncorrect username or password.")
