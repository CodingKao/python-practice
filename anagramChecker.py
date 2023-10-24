# Anagram Checker

# Ask user to enter a word
word_1 = input('Enter the first word: ')
word_2 = input('Enter the second word: ')

# convert string words into a list of letters
word_1_letters = list(word_1)
word_2_letters = list(word_2)

# sort each letter in the list
word_1_sorted = word_1_letters.sort()
word_2_sorted = word_2_letters.sort()

# print output of sorted letters
print(word_1_letters)
print(word_2_letters)

# print 
if word_1_letters == word_2_letters:
    print(f'"{word_1}" and "{word_2}" are anagrams.')
else:
    print(f'"{word_1}" and "{word_2}" are not anagrams.')
