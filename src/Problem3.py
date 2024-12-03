from Problem1 import MENU_AND_ROLE, justInvestMenu, privileges
from Problem2 import update_password_file

import getpass
import re

# source : https://en.wikipedia.org/wiki/Wikipedia:10,000_most_common_passwords , https://www.geeksforgeeks.org/python-program-check-validity-password/

PASSWORDS = "docs/passwd.txt"
COMMON_PASSWORDS = "docs/common_passwords.txt"

# PROBLEM 3b - password checker
def is_password_valid(username: str, password: str):
    if password == username:
        print("Password cannot be the same as username")
        return False
    elif is_common_password(password, COMMON_PASSWORDS): 
        # checks if password is part of top 10,000 common passwords
        print("Password is too common. Please choose a stronger password.\nRecommended: 8-12 characters, one uppercase and lowercase letter and one special character (!, @, #, $, %, *, &)")
        return False
    elif not (8 <= len(password) <= 12):
        print(f"Password must be between 8 and 12 characters long, your password is: {len(password)}")
        return False
    elif not re.search("[A-Z]", password):  
        print("Password must contain at least one uppercase letter")
        return False
    elif not re.search("[a-z]", password):  
        print("Password must contain at least one lowercase letter")
        return False
    elif not re.search("\d", password): 
        print("Password must contain at least one digit")
        return False
    elif not re.search("[!@#$%*&]", password): 
        print("Password must contain at least one special character from (!, @, #, $, %, *, &)")
        return False
    else:
        print("Password Valid!")
        return True 
    
# check if the password is common based on wikipedia's list of common passwords
def is_common_password(password, common_password_file):
    with open(common_password_file, 'r') as file:
        common_passwords = set(file.read().strip().split(","))
        return password in common_passwords

# check if role exists
def is_role_valid(role: str):
    case_insensitive = {key.lower(): value for key, value in MENU_AND_ROLE.items()}
    if case_insensitive.get(role) != None:
        print("Given role is a valid role")
        return True
    else:
        print("Given role is not a valid role")
        return False

# check if the given username already exists in the passwords file
def is_username_valid(username: str):
    with open(PASSWORDS, 'r') as file:
        for line in file:
            stored_username = line.split(',')[1].strip()
            if stored_username == username:
                print("Given username is not valid")
                return False
    print("Given username is valid!")
    return True

# PROBLEM 3a - sign up user interface
def sign_up(): 
    print("-"*50, "\nSign up: ")
    name = input("Enter your name: ")
    for available_roles in MENU_AND_ROLE.keys():
        print(f"- {available_roles}")
    role = input("Enter your role: ")
    username = input("Enter your username: ")
    print("Recommended: 8-12 characters, one uppercase and lowercase letter and one special character (!, @, #, $, %, *, &)")
    # hidden password input
    password = getpass.getpass("Enter your password (Hidden for security): ")

    # proactive password checker, alongside checks for username duplicates and role is a real role
    if is_password_valid(username, password) and is_role_valid(role) and is_username_valid(username):
        update_password_file(username, name, role, password) # adds new user to the password file
        privileges(username, role.title())
        justInvestMenu(role.title()) # automatically log in after sign up
    else: # not a proper input for any values 
        print("One of the inputted values were not a valid input.")