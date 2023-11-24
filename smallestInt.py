# Find the smallest integer in the array

# Input an array of integers, use commas to separate integers
array_input = input("Enter a set of numbers (separated by commas): ")

# Convert the input string to a list of integers
array = [int(x) for x in array_input.split(',')]

# Function to find the smallest integer in the array
def find_smallest_integer(array):
    # Use the min() function to find the smallest integer
    smallest_int = min(array)

    return smallest_int

print(find_smallest_integer(array))
