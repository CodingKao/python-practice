# Given an array of integers, return a new array with each value doubled.

# Ask user to create a new array
array_input = input("Enter an series of numbers (seperated by a space): ")

# Convert the input to a list of integers
array = list(map(int, array_input.split()))

# Define the function
def double_array(array):
    return [2 * x for x in array]

# Print output
print(double_array(array))