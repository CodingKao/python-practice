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


print("Exercise 8: Reserver String")
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



# Exercise 9: Count Vowels


# Exercise 10: Pattern Printing


# Exercise 11: Sum of squares





