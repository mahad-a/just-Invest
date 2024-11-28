import re
from datetime import datetime

# RBAC
MENU_AND_ROLE = {
    "Client": [
        "View account balance", 
        "View investment portfolio", 
        "View Finanical Advisor contact info"
    ],
    "Premium Client": [
        "Modify investment portfolio", 
        "View Finanical Planner contact"
    ],
    "Teller": [
        "View Client's account balance", 
        "View Client's investment portfolio"
    ],
    "Financial Advisor": [
        "View Client's account balance", 
        "View Client's investment portfolio", 
        "Modify Client's investment portfolio", 
        "View private consumer instruments"
    ],
    "Financial Planner": [
        "View Client's account balance", 
        "View Client's investment portfolio", 
        "Modify Client's investment portfolio", 
        "View money market instruments", 
        "View private consumer instruments"
    ],
}

ROLE_HIERARCHY = {
    "Client": [],
    "Premium Client": ["Client"],
    "Teller": ["Client"],
    "Financial Advisor": ["Teller"],
    "Financial Planner": ["Financial Advisor"],
}

# text files
SAMPLE = "docs/sample.txt"
PASSWORDS = "docs/passwd.txt"

def is_password_valid(username: str, password: str):
    if password == username:
        print("Password cannot be the same as username")
        return False
    elif not (8 <= len(password) <= 12):
        print(f"Password must be between 8 and 12 characters long, your password is: {len(password)}")
        return False
    elif not re.search("[A-Z]", password):  
        print("Password must contain at least one uppercase letter.")
        return False
    elif not re.search("[a-z]", password):  
        print("Password must contain at least one lowercase letter.")
        return False
    elif not re.search("\d", password): 
        print("Password must contain at least one digit.")
        return False
    elif not re.search("[!@#$%*&]", password): 
        print("Password must contain at least one special character from (!, @, #, $, %, *, &).")
        return False
    else:
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


def can_access(user_role, action):
    if user_role == "Teller" and not is_business_hours():
        return "NO ACCESS OUTSIDE BUSINESS HOURS"
    return action in get_access(user_role)

def is_business_hours():
    now = datetime.now()
    return now.hour >= 9 and now.hour < 17 # between 9:00am and 5:00pm or 9:00 and 17:00

def get_access(user_role):
    access = set(MENU_AND_ROLE.get(user_role))
    for inherited_access in ROLE_HIERARCHY.get(user_role):
        access.update(get_access(inherited_access))
    return access