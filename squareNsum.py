# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# Define function
def square_sum(numbers):
    # Convert input string to a list of integers
    numbers = [int(num) for num in numbers.split()]

    # Square each number in the list using list comprehension
    square_numbers = [num ** 2 for num in numbers]

    # Sum the squared numbers using the sum() function
    result = sum(square_numbers)

    return result

# Take input from the user
numbers_input = input("Enter some numbers (separated by spaces): ")

# Call the function and print the result
result = square_sum(numbers_input)
print(result)
