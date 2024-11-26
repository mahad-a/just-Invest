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
    if MENU_AND_ROLE.get(role) != None:
        return True
    else:
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
    

# def sign_up():
#     print("Sign up: ")
#     name = input("Enter your name: ")
#     role = input("Enter your role: ")
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")

#     if is_role_valid(role):
#         encrypt_password(password)
#         with open(PASSWORDS, 'a') as password_file:



if __name__ == "__main__":
    # justInvest("Client")
    # users = load_sample_users('docs/sample.txt')
    # for user in users:
    #     print(user)
    # print("-"*50)

    password = "hassan"
    encrypt_password(password)

    # username = input("Enter Username: ")
    # password = input("Enter Password: ")
    # # Test the function
    # user = "mahad"
    # is_password_valid(user, "mahad")        # Password == username (should fail)
    # is_password_valid(user, "mahad123")     # Missing special char (should fail)
    # is_password_valid(user, "mahad123!!")   # Valid password (should pass)
    # is_password_valid(user, "Mahad")        # Missing digits (should fail)
    # is_password_valid(user, "Mahad123!!")   # Valid password (should pass)
    