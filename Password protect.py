# Password-security-python
import hashlib

# define a function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# the correct password (you would typically store this securely in a database or file)
correct_password = hash_password('mysecretpassword')

# ask the user to enter their password
user_password = input('Please enter your password: ')

# hash the user's password
hashed_user_password = hash_password(user_password)

# check if the user's password matches the correct password
if hashed_user_password == correct_password:
    print('Access granted')
else:
    print('Access denied')
