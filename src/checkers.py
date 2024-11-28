import re
from datetime import datetime
from constants import *

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

def process_user_selection(user_input, index):
    while True:
        if 0 < int(user_input) <= index:
            print("Loading...")
            return int(user_input)
        else:
            print("Invalid input, try again.")
            user_input = input("Enter your option: ")