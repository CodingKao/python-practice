# String comparisons guess a letter

# Assign a letter to a variable to servce as the secret answer
secret = "x"

# Ask user to enter a letter, assign it to a variable
guess = input('Guess a letter from a-z: ')

# Compare user guess to secret letter
if guess == secret:
    print(f'You guessed the secret letter {secret}! ')
else: 
    print(f'Your guess was incorrect.  The secret letter was {secret}.')

# Letters in a word comparison

# ask user for a word and letter
word = input('Please enter a word: ')
letter = input('Please enter a letter from a-z: ')

# use IN to determine if letter is in word
if letter in word:
    print(f'The letter "{letter.upper()}" is in the word "{word}".')
else:
    print(f'The letter "{letter.upper()}" is not in the word "{word}".')

# If word contains the letter, tell user how many times the letters is in the word

# ask user to enter word and letter
word_2 = input('Please enter a word: ')
letter_2 = input('Please enter a letter: ')

# use keyword to to determine if letter is in word
# tell user how many times the letter apprears in the word

if letter_2 in word_2:
    # count the occurances of the letter in the word
    letter_2_count = word_2.count(letter_2)
    print(f'The word "{word_2}" contains the letter "{letter_2.upper()}" {letter_2_count} times.')
else:
    print(f'The letter {letter_2.upper()} is not in the word {word_2}.')






    