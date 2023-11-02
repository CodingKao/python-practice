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