# Define add function
def add(a, b):
    return a + b

# Define subtract function
def subtract(a, b):
    return a - b

# Define multiply function
def multiply(a, b):
    return a * b

# Define divide function
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Create the REPL
while True:
    operation = input("Enter the operation you would like to perform or type 'done' to quit: ")

    if operation == 'done':
        print('Goodbye')
        break

    operand_1 = input('Enter the first operand: ')
    operand_2 = input('Enter the second operand: ')

    try:
        operand_1 = float(operand_1)
        operand_2 = float(operand_2)

        if operation == '+':
            result = add(operand_1, operand_2)
        elif operation == '-':
            result = subtract(operand_1, operand_2)
        elif operation == '*':
            result = multiply(operand_1, operand_2)
        elif operation == '/':
            result = divide(operand_1, operand_2)
        else:
            result = "Invalid operation"

        print(f'{operand_1} {operation} {operand_2} = {result}')
    except ValueError:
        print('Please enter valid numbers for operands.')
