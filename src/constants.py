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