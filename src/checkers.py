import re

# RBAC
MENU_AND_ROLE = {
    "Client": ["View account balance", "View investment portfolio", "View Finanical Advisor contact info"],
    "Premium Client": ["Modify investment portfolio", "View Finanical Planner contact"],
    "Financial Advisor": ["View Client's account balance", "View Client's investment portfolio", "Modify Client's investment portfolio", "View private consumer instruments"],
    "Financial Planner": ["View Client's account balance", "View Client's investment portfolio", "Modify Client's investment portfolio", "View money market instruments", "View private consumer instruments"],
    "Teller": ["View Client's account balance", "View Client's investment portfolio"],
}

# text files
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
    case_insensitive = {key.lower(): value for key, value in MENU_AND_ROLE.items()}
    if case_insensitive.get(role) != None:
        print("Given role is a valid role")
        return True
    else:
        print("Given role is not a valid role")
        return False


def access_permission(user_role, action):
    return action in MENU_AND_ROLE.get(user_role)