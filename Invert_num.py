# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

def invert(lst):
    return [-num for num in lst]


numbers = [1, -2, 3, -4, 5]

result = invert(numbers)
print(f"The inverse of {numbers} is {result}")

user_input = input("Try it yourself.  Enter a set of numbers (seperated by a comma): ")
user_list = [int(num) for num in user_input.split(',')]
user_result = invert(user_list)

print(f"The inverse of {user_list} is {user_result}")