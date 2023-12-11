# Given an array, return the sum of the positive numbers and the sum of the negatives numbers

def sum_positive_and_negative(arr):
    # Initializ sums for positive and negative numbers
    sum_positives = 0
    sum_negatives = 0

    # Iterate through the array
    for num in arr:
        if num > 0:
            # add positive numbers to the positive sum
            sum_positives += num
        elif num < 0:
            # add negative numbers to the negative sum
            sum_negatives += num
    
    return sum_positives, sum_negatives

# Ask user for array of numbers
user_input = input("Enter five positive numbers and five negative numbers: ")

# Convert user input to a list of integers
user_numbers = [int(num) for num in user_input.split()]

# Call the function with the user's numbers
results = sum_positive_and_negative(user_numbers)

print(f"Sum of positives: {results[0]}, Sum of negatives: {results[1]}")