# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.


# Def function
def double_char(word):
    result = ''
    for char in word:
        result += char * 2
    
    return result

# Ask user for input
word = input("Enter a word: ")

print(double_char(word))