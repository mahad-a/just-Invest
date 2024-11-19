MENU_AND_ROLE = {
    "Client": ["View account balance", "View investment portfolio", "View Finanical Advisor contact info"],
    "Premium Client": ["Modify investment portfolio", "View Finanical Planner contact"],
    "Financial Advisor": ["View Client's account balance", "View Client's investment portfolio", "Modify Client's investment portfolio", "View private consumer instruments"],
    "Financial Planner": ["View Client's account balance", "View Client's investment portfolio", "Modify Client's investment portfolio", "View money market instruments", "View private consumer instruments"],
    "Teller": ["View Client's account balance", "View Client's investment portfolio"],
}

def justInvest(user_role):
    print("justInvest System\n", "-"*50, "\nOperations available on the system:")
    for idx, option in enumerate(MENU_AND_ROLE.get(user_role), start=1):
        print(f" {idx}. {option}")

def load_sample_users(filename):
    users = []
    with open(filename, 'r') as file:
        for line in file:
            name, role = line.strip().split(',')
            users.append({
                "Name": name, 
                "Role": role
            })
    return users

def access_permission(user_role, action):
    return action in MENU_AND_ROLE.get(user_role)
    

if __name__ == "__main__":
    justInvest("Client")
    users = load_sample_users('docs/sample.txt')
    for user in users:
        print(user)
