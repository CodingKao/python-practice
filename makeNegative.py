# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

# Ask user to enter a number
number = float(input("Enter a number: " ))

def make_negative(number):
    # check if number is already negative
    if number < 0:
        return number
    else:
        return -number
    
result = make_negative(number)
print("Your number is: " + str(result))
