# Guess the number

# import random module
import random

# secret number
secret = 5

# ask the user to guess
guess = input('Guess a number 1-10: ')

# convert guess to an integer for comparisons
guess = int(guess)

if guess < 1 or guess > 10:
    message = f'Invalid guess: {guess}.'

# if they guess correctly
elif guess == secret:
    message = f'You guessed the secret!'

# if they guess too high
elif guess > secret:
    message = f'Your guess of {guess} was too high!!'

# if they guess too low
elif guess < secret:
    message = f'Your guess of {guess} was too low!!'

# display result with a new line
print('\n' + message)
print(f'The secret was: {secret}')

# Generate a random integer between 1 and 1- to act as a secret number.

# random secret number
secret = random.randint(1, 10)

# loop until the user guesses the secret
while True:
    # ask the user to guess
    guess = input('\nGuess a number 1-10: ')

    # convert guess to an integer for comparisons
    guess = int(guess)

    if guess < 1 or guess > 10:
        message = f'Invalid guess: {guess}.'
        print(message)
        # go to the top of the loop
        continue

    # if they guess correctly
    elif guess == secret:
        message = f'You guessed the secret number: {secret}!'

        # display the winning message
        print(message)

        # end the loop
        break

    # if they guess too high
    elif guess > secret:
        message = f'Your guess of {guess} was too high!!'

    # if they guess too low
    elif guess < secret:
        message = f'Your guess of {guess} was too low!!'

    print(message)

# Allow the user three guesses. If they don't guess within three guesses, game over!

# random secret number
secret = random.randint(1, 10)

# number of guesses
guesses_remaining = 3

# loop until no guesses remain
while guesses_remaining > 0:
    # display the remaining guesses
    print(f'You have {guesses_remaining} guesses remaining.')

    # ask the user to guess
    guess = input('\nGuess a number 1-10: ')

    # convert the guess to an integer for comparisons
    guess = int(guess)

    if guess < 1 or guess > 10:
        message = (f'Invalid guess: {guess}.')
        print(message)
        # go to the top of the loop
        continue

    # if they guess correctly
    elif guess == secret:
        message = f'You guessed the secret number: {secret}!'

        # display the winning message
        print(message)

        # end the loop
        break

    # if they guess too high
    elif guess > secret:
        message = f'Your guess of {guess} was too high!!'

    # if they guess too low
    elif guess < secret:
        message = f'Your guess of {guess} was too low!!'

    # if the guess was too high or low,
    # remove a guess
    guesses_remaining -= 1
    print(message)

# when the user runs out of guesses
else:
    print(f'Sorry! You ran out of guesses. The secret was {secret}.')
