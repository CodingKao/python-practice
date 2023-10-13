# REPL, Functions

# Create function
def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# store input in list
number_list = []

# code to end loop when the user enters 'done'
while True:
    # user input
    user_input = input('Enter a number or "done" to quit: ')

    # check if the user is done
    if user_input == 'done':
        break  # end the loop

    # add the number to the list
    number_list.append(int(user_input))

    # print the running sum
    sum_num = sum(number_list)
    print(f'You entered {number_list}')
    print(f'The running sum of the numbers is: {sum_num}')

# print the final sum
print(f'Final sum of the numbers is: {sum_num}')
