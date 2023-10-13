# Count the loops
''' Construct a Read, Evaluate, Print, Loop (REPL) which performs the following on each iteration of the loops:
- Increment a counter variable to keep track of the number of loops.
- Ask the user if they would like to loop again,
- If the user enters 'yes', repeat the loop
- If the user enters 'no', end the loop and display the number of loops performed.
'''

# REPL loop

# create a counter
counter = 0

# begin a REPL
while True:
    # count the current iteration
    counter += 1

    # ask the user if they want to run the loop again
    again = input('Again? yes/no: ')

    # if the user enters 'no'
    if again == 'no':
        # tell the user how many times the loop ran
        print(f'The loop ran {counter} times.')

        # end the loop
        break
