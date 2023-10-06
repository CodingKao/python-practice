'''
Use string methods to determine the number of times 
a letter occurs in a word
'''
word = 'bookkeeper'
letter = 'k'

# use the .count() string method to count the occurrences of the letter in the word
letter_count = word.count(letter)

print(f"The letter '{letter}' occurs in the word '{word}' {letter_count} times.")


'''
Ask the user for a word
Ask the user for a letter
Assign the word and the letter to variables
Determine how many times the letter occurs in the word
'''
# get a word and a letter from the user
word = input('Please enter a word: ')
letter = input('Please enter a letter: ')

#use the .count() string method to count the occurrences of the letter in the word
letter_count = word.count(letter)

print(f"The letter '{letter}' occurs in the word '{word}' {letter_count} times.")