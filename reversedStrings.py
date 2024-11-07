# Complete the solution so that it reverses the string passed into it.

# Ask user to enter a word
string = input("Enter a word: ")


# Define the function
def solution(string):
    # Use slicing to reverse the string
    reversed_string = string[::-1]
    return reversed_string

# Print reversed string back to user
print(solution(string))

# Enter a sentence
sentence = input("Enter a sentence: ") 

# Define the function
def solution(sentence):
    #Split the sentence into words
    words = sentence.split()

    # Reverse the list of words
    reversed_words = words[::-1]

    # Join the reversed words back into a string
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

# Print the revesed string back to the user
print(solution(sentence))

# Reverse number
# Ask the user to input a series of numbers
numbers = input("Enter a series of numbers: ")

def reverse_numbers():
    # Split the input into a list of numbers (as strings)
    number_list = numbers.split()

    # Reverse the digits of each number in the list
    reversed_numbers = [num[::-1] for num in number_list]

    # Join the reversed numbers into a string with spaces
    return ' '.join(reversed_numbers)

# Call the function and print the reversed numbers
print("Reversed numbers:", reverse_numbers())