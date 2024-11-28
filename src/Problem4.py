import getpass
from Problem1 import *
from Problem1 import justInvestMenu
from constants import *
import bcrypt

def log_in(): # simple login user interface
    print("-"*50, "\nLog in: ")    
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password (Hidden for security): ")
    with open(PASSWORDS, "r") as file:
        for line in file:
            stored_name, stored_username,stored_role, stored_password_hash = line.strip().split(",")

            if username == stored_username:
                if bcrypt.checkpw(password.encode("utf-8"), stored_password_hash.encode("utf-8")):
                    print("ACCESS GRANTED!\nLogin successful! Welcome %s" % stored_name)
                    justInvestMenu(stored_role) # display options based on user's role
                    return
                else:
                    print("ACCESS DENIED!\nIncorrect password.")
    print("Username not found.")
    return