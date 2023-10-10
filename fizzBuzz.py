# Fizz Buzz

# Use a loop to create a list of numbers from 1 to 100
j = 0
while j < 100:
    # if multiple of 3 and 5

    # if j % 3 == 0 and j % 5 == 0:
    if j % 15 == 0:
        output = 'FizzBuzz'

    #  if multiple of 3
    elif j % 3 == 0:
        output = 'Fizz'

    # if multiple of 5
    elif j % 5 == 0:
        output = 'Buzz'

    # if not a multiple of 3' or 5'
    else:
        output = j
    
    # display the result each loop
    print(output)

    # count up
    j += 1