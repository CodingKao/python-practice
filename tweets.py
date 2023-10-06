# Import math module
import math

# Number of characters in tweet message
num_characters = 1345

# Max number of characters in a tweet (280)
max_characters = 280

# 3.1 Calculate the number of Tweets required, rounding up to the nearest integer.
tweets_needed = math.ceil(num_characters / max_characters)

print(f'''A message with {num_characters} characters, 
will need {tweets_needed} tweets.
''')

# 3.2 Ask the user for the number of characters in their message
# If the length of the message is less than the max_length allowed for a Tweet,
# output a message telling the user they only need one Tweet.
# Otherwise, calculate the number of Tweets required, rounding up to the nearest integer,
# and output a message telling the user the number of Tweets they will need.

# Ask user for the number of characters in the message
characters_required = input('Enter the number of characters in the message: ')

# Convert to an integer to perform math operations and comparisons
characters_required = int(characters_required)

# Calculate the number of tweets needed, rounding up with math.ceil()
tweets_required = math.ceil(characters_required / max_characters)

# If characters in the message are less than 280 characters
if characters_required <= max_characters:
    print(f'A message with {characters_required} characters only requires one Tweet!')
else:
    # Calculate the number of tweets needed, rounding up with math.ceil()
    tweets_required = math.ceil(characters_required / max_characters)
    print(f'A message with {characters_required} characters will need {tweets_required} tweets.')

# 3.3 Display different messages to the user depending on how many Tweets their message requires.
if tweets_required < 3:
    comment = "That shouldn't take you too long!"
elif tweets_required < 10:
    comment = "You'd better get typing!"
else:
    comment = "Maybe you should find a different way..."

# Create the message with commas in appropriate places for characters count
message = f'''
A message containing {characters_required:,} characters
will require {tweets_required} tweets.
'''

# Add comment to the message
message += comment

print(message)
