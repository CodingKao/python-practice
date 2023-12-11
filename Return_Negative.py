# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

# Defind function
def make_negative (number):
    return -number if number > 0 else number

user_input = input("Enter a number: ")
number = int(user_input)

print(make_negative(number))