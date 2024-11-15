def assign_role(user_input):
    if user_input == "1":
        return "Client"
    elif user_input == "2":
        return "Premium Client"
    elif user_input == "3":
        return "Financial Advisor"
    elif user_input == "4":
        return "Financial Planner"
    elif user_input == "5":
        return "Teller"
    else: # if user fails to provide a proper input
        return "Client"

## example of menu and inputs (for later implementation)
# print("Choose your role:")
# print("1. Client")
# print("2. Premium Client")
# print("3. Financial Advisor")
# print("4. Financial Planner")
# print("5. Teller")

# user_choice = input("Enter the number corresponding to your role: ")
# user_role = assign_role(user_choice)
