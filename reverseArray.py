# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Ask the user to enter a series of numbers
number = int(input("Enter a number: "))

def digitize(n):
    return [int(digit) for digit in str(n)[::-1]]

print(digitize(number))