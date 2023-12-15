# Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

# Define the function
def repeat_letter_in_word(letter, repeat, word):
    # Repeat the letter
    repeated_letter = letter * repeat
    
    # Replace the first occurrence of the letter in the word with the repeated letter
    result_word = word.replace(letter, repeated_letter, 1)
    
    return result_word

# Ask user for input
letter = input("Enter a letter: ")
repeat = int(input(f"Enter the number of times to repeat the letter '{letter}' in the word: "))
word = input("Enter a word: ")

# Call the function with the correct arguments
result_word = repeat_letter_in_word(letter, repeat, word)

# Print the result
print(f"The letter '{letter}' will be repeated {repeat} times in the word '{word}'.")
print(f"The result is: {result_word}")