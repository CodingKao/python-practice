# Practice using While Loop
# A while loop in Python is a control flow structure that repeatedly executes a block of code as long as a specified condition is true. 

print("Exercise 1: Count up")
def count_up(number):
    count =1 
    while count <= number:
        print(count)
        count += 1

# Get user input
user_input = input("Enter a number to count up to: ")
user_number = int(user_input)

# print result
count_up(user_number)