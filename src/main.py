import bcrypt
import re

MENU_AND_ROLE = {
    "Client": ["View account balance", "View investment portfolio", "View Finanical Advisor contact info"],
    "Premium Client": ["Modify investment portfolio", "View Finanical Planner contact"],
    "Financial Advisor": ["View Client's account balance", "View Client's investment portfolio", "Modify Client's investment portfolio", "View private consumer instruments"],
    "Financial Planner": ["View Client's account balance", "View Client's investment portfolio", "Modify Client's investment portfolio", "View money market instruments", "View private consumer instruments"],
    "Teller": ["View Client's account balance", "View Client's investment portfolio"],
}

SAMPLE = "docs/sample.txt"
PASSWORDS = "docs/passwd.txt"

class User:
    def __init__(self, name, username, role):
        self.name = name
        self.username = username
        self.role = role
    
    def get_name(self):
        return self.name
    
    def get_username(self):
        return self.username
    
    def get_role(self):
        return self.role

def is_password_valid(username: str, password: str):
    if password == username:
        print("Password cannot be the same as username")
        return False
    
    if not (8 <= len(password) <= 12):
        print(f"Password must be between 8 and 12 characters long, your password is: {len(password)}")
        return False
    
    if not re.search(r'[A-Z]', password):  
        print("Password must contain at least one uppercase letter.")
        return False
    if not re.search(r'[a-z]', password):  
        print("Password must contain at least one lowercase letter.")
        return False
    if not re.search(r'\d', password): 
        print("Password must contain at least one digit.")
        return False
    if not re.search(r'[!@#$%*&]', password): 
        print("Password must contain at least one special character from (!, @, #, $, %, *, &).")
        return False

    print("Password Valid!")
    return True 

def is_role_valid(role: str):
    case_insensitive = {key.lower(): value for key, value in MENU_AND_ROLE.items()}
    if case_insensitive.get(role) != None:
        print("Given role is a valid role")
        return True
    else:
        print("Given role is not a valid role")
        return False

def justInvest(user_role):

    print("justInvest System\n", "-"*50, "\nOperations available on the system:")
    for idx, option in enumerate(MENU_AND_ROLE.get(user_role), start=1):
        print(f" {idx}. {option}")

def load_sample_users(filename):
    users = []
    with open(filename, 'r') as file:
        for line in file:
            name, role, username, password = line.strip().split(',')
            users.append({
                "Name": name, 
                "Role": role,
                "Username": username,
                "Password": password
            })
    return users

def access_permission(user_role, action):
    return action in MENU_AND_ROLE.get(user_role)

def encrypt_password(password: str):
    password_byte = password.encode("utf-8") # encode password in bytes
    print(password_byte)
    hash_result = bcrypt.hashpw(password_byte, bcrypt.gensalt(rounds=10)) # hash the password and add salt
    print(hash_result)
    # with open("passwd.txt", 'a') as file:
    #     file.write("Username: %s, Password: %d" % (username, hash_result))
    if bcrypt.checkpw(password_byte, hash_result):
        return hash_result

def sign_up():
    # while True:
    print("-"*50)
    print("Sign up: ")
    name = input("Enter your name: ")
    for available_roles in MENU_AND_ROLE.keys():
        print(f"- {available_roles}")
    role = input("Enter your role: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if is_password_valid(username, password) and is_role_valid(role):
        hashed_password = encrypt_password(password)
        with open(PASSWORDS, 'a') as password_file:
            password_file.write("Name: %s, Username: %s, Role: %s, Password: %s" % (name.title(), username, role.title(), hashed_password.decode("utf-8")))
            justInvest(role.title())
            # break
    else:
        print("One of the inputted values were not a valid input.")
    print("-"*50)

def log_in():
    print("-"*50)
    print("Log in: ")
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open(PASSWORDS, "r") as file:
        content = file.read()
        stored_name = content.split(',')[0].split(':')[1].strip()
        stored_username = content.split(',')[1].split(':')[1].strip()
        stored_role = content.split(',')[2].split(':')[1].strip()
        stored_password_hash = content.split(',')[3].split(':')[1].strip()

        if username == stored_username:
            if bcrypt.checkpw(password.encode("utf-8"), stored_password_hash.encode("utf-8")):
                print("Login successful! Welcome %s" % stored_name)
                justInvest(stored_role)
                return
            else:
                print("Incorrect password.")
    print("Username not found.")
    return


if __name__ == "__main__":
    print("-" * 50)
    print("Main Menu")
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

        