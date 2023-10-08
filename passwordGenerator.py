# Password Generator

#import module
import random
import string

# concat all character types (letters, digits, punctuation)
letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

all_characters = letters + digits + punctuation

password = ""

while len(password) < 10:
    password += random.choice(all_characters)

print(password)

