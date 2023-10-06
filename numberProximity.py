# 4.1 Number Proximity

# Assign a number to a variable
number = 108

# Determine whether the number is within 10 of 100
is_within_10 = abs(number - 100) <= 10
message = f'{number} is {"within" if is_within_10 else "not within"} 10 of 100.'

print(message)

# 4.2 User Input for Number Comparison

# Have the user enter values for number_1 and number_2
number_1 = int(input('Enter a number: '))
number_2 = int(input('Enter another number: '))

# Determine which number is bigger and check if they are within 10 of each other
is_within_10 = abs(number_1 - number_2) <= 10
message = f'{number_1} is {"within" if is_within_10 else "not within"} 10 of {number_2}.'

print(message)

# 4.3 User Input for Number Proximity with Custom Threshold

# Have the user enter values for number_1, number_2, and the threshold
number_1 = int(input('Enter the first number: '))
number_2 = int(input('Enter the second number: '))
threshold = int(input('Enter how far apart the numbers are allowed to be: '))

# Use abs() to find the absolute value and check if they are within the threshold
is_within_threshold = abs(number_1 - number_2) <= threshold
message = f'{number_1} is {"within" if is_within_threshold else "not within"} {threshold} of {number_2}.'

print(message)

