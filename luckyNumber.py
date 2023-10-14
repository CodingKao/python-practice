# Help user calulate their lucky number

name = 'John'
number = len(name)*9
print("Hello " + name + ".  Your lucky number is " + str(number))

name = 'Doe'
number = len(name)*9
print("Hello " + name + ".  Your lucky number is " + str(number))

# Write function for resuable code
def lucky_number(name):
    number = len(name)*9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("John")
lucky_number("Doe")