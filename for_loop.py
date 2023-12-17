# Practice for loop

# Iterate from 1 - 5
print("Iterate 1 - 5")
# Using range() to iterate from 1 to 5
for number in range(1,6):
    print(number)
   
# Iterate from 1 - 10 with skip of 2    
print("Iterate 1-10 with a skip of 2")
# Add skip
for number in range(1,10,2):
    print(number)


# Iterate from 1 to 5 and add the sum
print("Iterate 1-10 and add the sum")
# Initialize a variable to store the sum
sum_of_numbers = 0

# Use a for loop to iterate through numbers from 1 to 10
for number in range(1, 11):
    # add each number to the sum
    sum_of_numbers += number
print("Sum of numbers from 1 to 10: ", sum_of_numbers)