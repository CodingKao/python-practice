# Fibonacci / Tribonacci

# write a loop that adds the first 10 values of the fibonacci sequence to a list

# starting values
fibonacci = [0,1]

i = 0 #index counter

# while fibonacci list has less than ten elements
while len(fibonacci) < 10:

    # get the two previous numbers
    prev_1 = fibonacci[i]
    prev_2 = fibonacci[i+1]

    # sum of the two previoius numbers
    n = prev_1 + prev_2

    # add n to the list
    fibonacci.append(n)

    # increase i
    i += 1

# display the result
output = f'First ten Fibnoacci numbers: \n{fibonacci}'
print(output)

# Create a new list of Tri-boancci values where each 
# consecutive number is the sum of the previous three numbers

# starting values 
tribonacci = [0,1,1]

# index counter
i = 0 

# while fibonacci has less than ten elements
while len(tribonacci) < 10:

    # get the three previous numbers
    prev_1 = tribonacci[i]
    prev_2 = tribonacci[i+1]
    prev_3 = tribonacci[i+2]

    # sum of the three previous numbers
    n = prev_1 + prev_2 + prev_3

    # add n to the list
    tribonacci.append(n)

    # increase i
    i += 1

# display the result
output = f'First ten Tribonacci numbers: \n{tribonacci}'
print(output)

# Write both the Fibonacci and Tribonacci sequence loops 
# without providing the first two three starting values

# no starting values
fibonacci = []

i = 0 # index counter

# while fibonacci has less than ten elements
while len(fibonacci) < 10:

    # get the first two elements
    if len(fibonacci) < 2:

        # len(fibonacci) with be either 0 or 1,
        # so the first two elements become [0,1]
        n = len(fibonacci)

    # calculate all other elements
    else:
        # get the twp previous elements
        prev_1 = fibonacci[i]
        prev_2 = fibonacci[i+1]

        # add the sum of the three previous numbers to the list
        n = prev_1 + prev_2

        # increase i
        i += 1

    # add n to the list
    fibonacci.append(n)

# display the result
output = f'First ten Fibonacci numbers: \n{fibonacci}'
print(output)

# no starting values
tribonacci = []

i = 0 # index counter

# while tribonaccit has less than ten elements
while len(tribonacci) < 10:
    # get the first two elements
    if len(tribonacci) < 2:
        # the first two elements become [0,1]
        # because the length is less than 2 (0 or 1)
        n = len(tribonacci)

    # get the third element
    elif len(tribonacci) == 2:
        n=1

    # calculate all other elements
    else:
        # get the three previous numbers
        prev_1 = tribonacci[i]
        prev_2 = tribonacci[i+1]
        prev_3 = tribonacci[i+2]

        # sum of the three previous numbers
        n = prev_1 + prev_2 + prev_3

        # i += 1

    # add n to the list
    tribonacci.append(n)

# display the result
output = f'First ten Tribonacci numbers:\n{tribonacci}'
print(output)

# Allow the user to enter the number of elements to calculate
# in both the Fibonacci and Tribonacci loops

# ask the user for the number of elements
limit = input("Enter the number of Fibonacci numbers you'd like to generate: ")

# convert the input to an integer
limit = int(limit)

# use the input value to set the loop
while len(tribonacci) < 10:
    # get the first two elements
    if len(tribonacci) < 2:
        # the first two elements become [0,1]
        # because the length is less than 2 (0 or 1)
        n = len(tribonacci)

    # get the third element
    elif len(tribonacci) == 2:
        n=1

    # calculate all other elements
    else:
        # get the three previous numbers
        prev_1 = tribonacci[i]
        prev_2 = tribonacci[i+1]
        prev_3 = tribonacci[i+2]

        # sum of the three previous numbers
        n = prev_1 + prev_2 + prev_3

        # i += 1

    # add n to the list
    tribonacci.append(n)

# display the result
output = f'First ten Tribonacci numbers:\n{tribonacci}'
print(output)

