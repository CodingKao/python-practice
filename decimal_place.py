# Each number should be formatted that it is rounded to two decimal places. You don't need to check whether the input is a valid number because only valid numbers are used in the tests.

# Def function
def format_number(number):
    return f"{number:.2F}"

#  Usage
number = 3.16345676543
formatted_number = format_number(number)
print(formatted_number)