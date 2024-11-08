# Reorder and count the number of letters based on an input by user

# Ask the user to enter a word
word = input("Enter a word or phrase: ".lower()) # Conver input to lowercase letter

# Function to reorder letters and count frequency
def reorder_and_count(word):
    # sort the letter in alphabetical order
    sorted_letters = ''.join(sorted(word))

    # count the frequency of each letter using a dictionary
    letter_count = {}
    for letter in sorted_letters:
        if letter in letter_count:
            letter_count[letter] += 1
        
        else:
            letter_count[letter] = 1

    return sorted_letters, letter_count

# Get the reordered letters and letter count
sorted_letters, letter_count, = reorder_and_count(word)

# Print the results
print("Letters in alphabetical order:", sorted_letters)
print("Letter frequencies:")

for letter, count in letter_count.items():
    print(f"{letter}: {count}")