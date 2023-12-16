# Check if value is in array

# Define the function
def check(seq, elem):
    return elem in seq

# Ask the user for the array
array_str = input("Enter the array (comma-separated values): ")
user_array = [float(x.strip()) if x.strip().replace('.', '').isdigit() else x.strip() for x in array_str.split(',')]

# Get user input for the value
user_value = input("Enter the value to check: ")

# Call the check function
result = check(user_array, user_value)

# Print the result
print(f"The array {user_array} {'contains' if result else 'does not contain'} the value {user_value}.")