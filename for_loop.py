# Practice for loop

# Exercise 1: Print numbers using for loop
print("Exercise 1: Print numbers using for loop")
# Using range() to iterate from 1 to 5
for number in range(1,6):
    print(number)
   
# Exercise 2: Print number using skip
print("Exercise 2: Print number using skip")
# Add skip
for number in range(1,10,2):
    print(number)


# Exercise 3: Sum of numbers 
print("Exercise 3: Sum of numbers ")
# Initialize a variable to store the sum
sum_of_numbers = 0

# Use a for loop to iterate through numbers from 1 to 10
for number in range(1, 11):
    # add each number to the sum
    sum_of_numbers += number
print("Sum of numbers from 1 to 10: ", sum_of_numbers)


# Exercise 4: Print even numbers
print("Exercise 4: Print even numbers")
for number in range(0, 21, 2):
    print(number)

# Exercise 5: Square Numbers
# initialize a variable to store the sum
sum_of_squares = 0    

print("Exercise 5: Square numbers")
for number in range(1,6):
    square = number ** 2
    print(square)

    sum_of_squares += square

print("Sum of the squares is: " ,sum_of_squares)

print("Exercise 6: Print the factorial of a number")
# Exercise 6: Factorial
def calculate_factorial(n):
    if n < 0:
        return "Factorial is undefined for negative numbers."
    
    factorial_result = 1

    # using a for loop to calculate the factorial
    for i in range(1, n + 1):
        factorial_result *= i

    return factorial_result

# Get user input with a limit of 10
number = int(input("Enter a non-negative number: "))
if 0 <= number <= 10:
    result = calculate_factorial(number)
    print(f"The factorial of {number} is {result}")
else: 
    print(f"Please enter a non-negative number less than or equal to 10.")


print("Exercise 7: Print the multiplication table of a number")
# Exercise 7: Multiplication table
def multiplication_table(n):
    if n < 1 or n > 10:
        return "Please enter a number between 1 and 10."

    # use for loop to calculate multiplication table
    for i in range(1, 11):
        result = n * i
        print(f"{n} x {i} = {result}")


# Get user input
number = int(input("Enter a number between 1 and 10: "))
multiplication_table(number)         


print("Exercise 8: Reverse String")
# Exercise 8: Reverse String
def reverse_string(input_string):
    reversed_result = ""

    # Use a for loop to reverse the string
    for char in input_string:
        reversed_result = char + reversed_result

    return reversed_result

# Get user input for the string
user_input = input("Enter a string to reverse: ")

# Reverse the string and print result
result = reverse_string(user_input)
print(f"The reversed string of {user_input} is: {result}")


print("Exercise 9: Count Vowels")
# Exercise 9: Count Vowels
def count_vowels(input_string):
    vowel_count = 0

    # Use a for loop to iterate each character in the input string
    for char in input_string:
        # check if the character is a vowel
        if char.lower() in "aeiou":
            vowel_count += 1

    return vowel_count

# Get user input for the string
user_input = input("Enter a string to count vowels: ")

# Count voewls in the string and print the result
result = count_vowels(user_input)
print(f"The number of vowels in the string is: {result}")

print("Exercise 10: Star Pattern Printing")
# Exercise 10: Star Pattern Printing
def print_star_pattern(rows):
    for i in range(1, rows + 1):
        print("*" * i)

# Get user input for the number of rows
num_rows = int(input("Enter the number of rows for the stars: "))

# Print the star pattern
print_star_pattern(num_rows)

print("Exercise 11: Count down")
# Exercise 11: Sum of squares
def count_down(counter):
    for i in range(counter, 0, -1):
        print(i)

# Ask user for input limit of 50
user_input = int(input("Enter a number for the countdown (limit 50): "))
    
# Check the user input
if user_input == 0:
    print("Enter a higher number for the countdown.")
elif user_input > 50:
    print("Enter a lower number for the countdown.")
else:
    # Print the countdown
    count_down(user_input)



