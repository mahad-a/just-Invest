import bcrypt # chosen hashing function

PASSWORDS = "docs/passwd.txt"

# PROBLEM 2a - selection of hashing function
def encrypt_password(password: str): 
    password_byte = password.encode("utf-8") # encode password in bytes
    hash_result = bcrypt.hashpw(password_byte, bcrypt.gensalt(rounds=10)) # hash the password and add salt
    if bcrypt.checkpw(password_byte, hash_result):
        return hash_result # returns the hashed password

# PROBLEM 2b and 2c (a) - creation of the password file and adding new users, part of Problem3.py (sign up)
def update_password_file(username, name, role, password):
    hashed_password = encrypt_password(password) # encrypt the new password by hashing and salting
    with open(PASSWORDS, 'a') as password_file: # add to password file
        password_file.write("%s,%s,%s,%s\n" % (name.title(), username, role.title(), hashed_password.decode("utf-8")))

# PROBLEM 2c (b) - retrieving users from password file, part of Problem4.py (log in)
def get_account_from_file(username, password):
    with open(PASSWORDS, "r") as file:
        for line in file:
            stored_name, stored_username, stored_role, stored_password_hash = line.strip().split(",")
            if username == stored_username:
                if bcrypt.checkpw(password.encode("utf-8"), stored_password_hash.encode("utf-8")):
                    return stored_name, stored_role
    return None