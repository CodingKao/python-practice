# Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero numbers.

# Define the function
def is_divisible(n, x, y):
    # Check if n is divisible by both x and y
    return n % x == 0 and n % y == 0

# Example values
n_example = 12
x_example = 2
y_example = 6

# Check if n is divisible by both x and y
result_output = is_divisible(n_example, x_example, y_example)

# Print the result
print(f"Is {n_example} divisible by both {x_example} and {y_example}? {result_output}")


