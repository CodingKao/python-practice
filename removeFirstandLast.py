# Remove First and Last Character

# Ask for user input
original_string = input("Please enter a word: ")


def remove_char(input_string):
    # Check if the string has at least two characters
    if len(input_string) >= 2:
        # Use string slicing to remove the first and last characters
        result_string = input_string[1:-1]
        return result_string
    else:
        # If the string has less than two characters, return the original string
        return input_string


result = remove_char(original_string)
print(result)
