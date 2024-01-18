# Practice using While Loop
# A while loop in Python is a control flow structure that repeatedly executes a block of code as long as a specified condition is true. 

print("Exercise 1: Count up")
def count_up(number):
    count = 1
    while count <= number:
        print(count)
        count += 1

# Get user input
user_input = input("Enter a number to count up to: ")
user_number = int(user_input)

# print result
count_up(user_number)

print("Exercise 2: Count down")
def count_down(start, stop):
    while start >= stop:
        print(start)
        start -= 1

# Get user input
start = int(input("Enter the starting number: "))
stop = int(input("Enter the stop number: "))

# Print result
count_down(start, stop)

print("Exercise 3: Repeat number")

# get user input
user_number = int(input("Enter a number to repeat: "))
repetition = int(input("Enter the number of times to repeat: "))

# set the counter
count = 0

while count < repetition:
    print(user_number)
    count += 1


print("Exercise 4: Print Even Numbers")
# get user input
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))

# validate the numbers are within parameters
while end_number < start_number:
    print("Ending number should be greater than or equal to the starting number")
    end_number = int(input("Enter the ending number: "))

# print even numbers using a while loop
current_number = start_number

while current_number <= end_number:
    if current_number % 2 == 0:
        print(current_number)
    current_number += 1

print("Exercise 5: Print Odd Numbers")
# get user input
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))

# validate the numbers are within parameters
while end_number < start_number:
    print("Ending number should be greater than or equal to starting number")
    end_number = int(input("Enter the ending number: "))

# print odd numbers using a while loop
current_number = start_number

while current_number <= end_number:
    if current_number % 2 != 0:
        print(current_number)
    current_number += 1

print("Exercise 6: Guess the Password")
# Set the correct password first
correct_password = "secret123"

# Ask user to guess the password
user_guess = input("Guess the Password: ")

# Use while loop to keep prompting until the correct password is guessed
while user_guess != correct_password:
    print("Incorrect password.  Try again.")
    user_guess = input("Guess the password: ")

# If user guess correctly, loop ends
print("Congratulations!  You've guessed the correct password. ")
                

print("Exercise 7: Fizz Buzz")
# Ask the user to enter an umber below 50
user_number = int(input("Enter a number below 50: "))

# Set the initial number
number = 1

# Use while loop to iterate up tot he user's entered number
while number <= user_number:
    # check for multiples of both 3 and 5
    if number % 3 == 0 and number % 5 ==0:
        print("FizzBuzz")
    
    # check for multiple of 3
    elif number % 3 == 0:
        print("Fizz")

    # check for multiples of 5
    elif number % 5 == 0:
        print("Buzz")

    # Print the number if not a multiple of 3 or 5
    else:
        print(number)

    # increment the number for the next iteration
    number += 1