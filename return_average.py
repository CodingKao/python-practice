# Write a function which calculates the average of the numbers in a given list.
# Note: Empty arrays should return 0.

# Define the function to calculate the average of the numbers in a given list
def find_average(numbers):
    if not numbers:
        return 0
    else:
        return sum(numbers) / len(numbers)

# Ask user to enter input
numbers_input = input("Enter a list of numbers (seperated by spaces): ")
numbers_list = [float(num) for num in numbers_input.split()]


print(find_average(numbers_list))