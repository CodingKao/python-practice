10# Import required modules
import random
import string

# Define a function called 'generate_password'
def generate_password(length):
    # Concatenate all character types (letters, digits, punctuation)
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''

    while len(password) < length:
        password += random.choice(all_characters)

    return password

# Prompt the user for the desired password length
try:
    length = int(input('Please enter the desired length of the password: '))
    if length <= 0:
        print('Password length must be a positive number.')
    else:
        password = generate_password(length)
        print(f'Generated password: {password}')
except ValueError:
    print('Please enter a valid number for the password length.')
