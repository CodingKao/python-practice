# Anagram Generator.  Write a code that lets user input letters with a maximum of 6 letters and code will give possible anagram.

# In the terminal --> Install and set up 'nltk'
# 'pip install nltk'

# import 'nltk'
import nltk
nltk.download('words')

import itertools
from nltk.corpus import words

# Load English words from nltk corpus
english_words = set(w.lower() for w in words.words())

# Step 1: Get User Input (Letters)
print("=== Anagram Generator ===")
letters = input("Enter up to 6 letters (no spaces): ").lower()

# Step 2: Check that the number of letters is valid
if len(letters) == 0 or len(letters) > 6:
    print("Invalid input. Please enter between 1 and 6 letters.")

else:
    # Step 3: Ask user for desired anagram length
    length_input = input("Enter desired anagram length (1 to {}): ".format(len(letters)))

    if not length_input.isdigit():
        print("Invalid input. Please enter a number.")
    else:
        length = int(length_input)

        # Step 4: Validate anagram length
        if length <= 0 or length > len(letters):
            print("Invalid length. Must be between 1 and", len(letters))
        else:
            # Step 5: Generate all possible permutations (anagrams) of the specified length
            anagrams = itertools.permutations(letters, length)

            # Step 6: Filter to include only valid English words
            valid_words = set()
            for a in anagrams:
                word = ''.join(a)
                if word in english_words:
                    valid_words.add(word)

            # Step 7: Display the results
            if valid_words:
                print("\nValid English words ({} letters long):".format(length))
                for word in sorted(valid_words):
                    print(word)
            else:
                print("No valid English words found.")
