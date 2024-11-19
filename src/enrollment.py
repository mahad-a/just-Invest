import re

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

# Test the function
user = "mahad"
is_password_valid(user, "mahad")        # Password == username (should fail)
is_password_valid(user, "mahad123")     # Missing special char (should fail)
is_password_valid(user, "mahad123!!")   # Valid password (should pass)
is_password_valid(user, "Mahad")        # Missing digits (should fail)
is_password_valid(user, "Mahad123!!")   # Valid password (should pass)
