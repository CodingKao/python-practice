# Define the function
def sum_array(array):
    if not array:
        return 0
    
    total_sum = sum(array)
    return total_sum

# Ask user to enter an array of numbers
input_str = input("Enter a set of numbers (separated by commas): ")

# Convert the input string into a list of numbers
array = [float(num) for num in input_str.split(',')]

# Call the function and print the result
result = sum_array(array)
print(f"The sum of the numbers is: {result}")

