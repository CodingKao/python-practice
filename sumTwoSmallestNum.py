# Sum Two Smallest Integers

user_input = input("Enter an array of numbers (separated by spaces): ")

# Split the user input into individual numbers and convert them to integers
numbers = [int(num) for num in user_input.split()]

def sum_two_smallest_numbers(numbers):
    # Check if the input list has at least 2 elements
    if len(numbers) < 2:
        return "Input list must contain at least 2 numbers"
    
    # Sort the input list in ascending order
    numbers.sort()
    
    # Sum the first two elements of the sorted list
    return numbers[0] + numbers[1]

result = sum_two_smallest_numbers(numbers)

# Check if the result is a valid number or an error message
if isinstance(result, int):
    print("Sum of the two smallest positive numbers:", result)
else:
    print(result)
