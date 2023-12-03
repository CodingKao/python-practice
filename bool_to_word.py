# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

# Define the function
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# User input

boolean = input("Enter True or False: ")

print(bool_to_word(bool))