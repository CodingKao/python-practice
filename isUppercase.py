# Is the string uppercase?
# Create a method to see whether the string is ALL CAPS.

def is_uppercase(inp):
    # Check if the input string has at least one alphabetical character
    if any(char.isalpha() for char in inp):
        # Check if the input string is in all uppercase letters
        return inp.isupper()
    else:
        return False

# Ask users to enter a word
text = input("Please enter a word: ")

# Example usage:
if is_uppercase(text):
    print("The string is in all capital letters.")
else:
    print("The string is not in all capital letters.")
