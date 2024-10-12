# Each number should be formatted that it is rounded to two decimal places. You don't need to check whether the input is a valid number because only valid numbers are used in the tests.

# Def function
def format_number(number):
    return f"{number:.2F}"

# Ask for user input
user_input = float(input("Enter a number with decimals: "))

# Round the input to the nerest whole number
rounded_number = round(user_input)

# Format the rounded number to two decimals places
formatted_number = format_number(user_input)

# Print results
print(f"Formatted to two decimal places: {formatted_number}")
print(f"Round to whole number: {rounded_number}")