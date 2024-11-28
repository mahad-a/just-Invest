import bcrypt # chosen hashing function


def encrypt_password(password: str):
    password_byte = password.encode("utf-8") # encode password in bytes
    hash_result = bcrypt.hashpw(password_byte, bcrypt.gensalt(rounds=10)) # hash the password and add salt
    if bcrypt.checkpw(password_byte, hash_result):
        return hash_result # returns the hashed password

# creation of the password file and adding new users are handled in Problem3.py
# retrieving users from password file is handled in Problem4.py