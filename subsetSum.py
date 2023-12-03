# Define the function
def find_numbers_for_sum(numbers, target_sum):
    # Convert the input string into a list of integers
    numbers = [int(num) for num in numbers.split(',')]
    
    # Iterate through all possible subsets of numbers
    for i in range(1, 2**len(numbers)):
        subset = [numbers[j] for j in range(len(numbers)) if (i >> j) & 1]
        if sum(subset) == target_sum:
            return subset
    return None

# Example usage:
user_input = input("Enter a set of numbers (separated by commas): ")
target_sum = int(input("Enter the target sum:"))  # Removed parentheses around 55

result = find_numbers_for_sum(user_input, target_sum)

if result:
    print(f"A subset of numbers that adds up to {target_sum}: {result}")
else:
    print("No subset found.")
