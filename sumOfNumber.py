# Ask the user to enter numbers separated by spaces
user_input = input("Enter the numbers you want to add (separated by spaces): ")

# Split the input into a list of numbers
numbers = [float(num) for num in user_input.split()]

def positive_sum(arr):
    # Initialize a variable to store the sum
    total = 0
    
    # Iterate through the array
    for num in arr:
        if num > 0:  # Check if the number is positive
            total += num  # Add the positive number to the sum
    
    return total  # Return the total sum

# Example usage:
result = positive_sum(numbers)
print("Sum of positive numbers:", result)
