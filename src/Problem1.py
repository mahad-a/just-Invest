from datetime import datetime

# PROBLEM 1a - selected RBAC as access control model
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

# part of the RBAC access control
ROLE_HIERARCHY = { # organize roles by hierachy, with each inheriting lower roles
    "Client": [],
    "Premium Client": ["Client"],
    "Teller": ["Client"],
    "Financial Advisor": ["Teller"],
    "Financial Planner": ["Financial Advisor"],
}

# check what the role can access
def can_access(user_role, action):
    # ensure Teller cannot access the system if not in business hours
    if user_role == "Teller" and not is_business_hours():
        return "NO ACCESS OUTSIDE BUSINESS HOURS"
    return action in get_access(user_role)

# check if currently in business hours or not
def is_business_hours():
    now = datetime.now()
    return now.hour >= 9 and now.hour < 17 # between 9:00am and 5:00pm or 9:00 and 17:00

# get set of user's access permissions based their role
def get_access(user_role):
    # set to avoid having duplicate permissions from inheriting lower roles
    access = set(MENU_AND_ROLE.get(user_role))
    for inherited_access in ROLE_HIERARCHY.get(user_role):
        access.update(get_access(inherited_access)) # recursion to continue to the bottom of the hierarchy
    return access

# process the user's input to ensure they put in a proper input
def process_user_selection(user_input, index):
    while True:
        if 0 < int(user_input) <= index:
            print("Loading...")
            return int(user_input)
        else:
            print("Invalid input, try again.")
            user_input = input("Enter your option: ")

# display the access privileges
def privileges(username, role):
    access_rights = get_access(role)
    print(f"Current Session:\nUsername: {username}\nRole: {role}\nAccess Rights: {access_rights}")

# the system menu once logged in
def justInvestMenu(user_role):
    print("justInvest System\n", "-"*50, "\nOperations available on the system:")
    menu = list(get_access(user_role)) # convert from set to list
    menu.append("Log out") # add log out option to list to ensure that its always last
    for idx, option in enumerate(menu, start=1):
        print(f" {idx}. {option}")
    user_input = input("Enter your option: ")
    result = process_user_selection(user_input, len(menu)) # process user's input for validation

    if result:
        selection = menu[result-1]
        if selection == "Log out": # log out the user and return to main menu
            print("Logging out...")
            from main import main_menu # to avoid circular imports, only import main_menu when it needs to be used
            main_menu()
        print("ACCESS GRANTED TO %s" % selection)