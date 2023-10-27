your_number = float(input("Enter a number: " ))

def even_or_odd(your_number):
    if your_number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example:
result = even_or_odd(your_number)
print("Your number is: " + result) 
