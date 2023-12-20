# Write a function that returns both the minimum and maximum number of the given list/array.


# Define the function
def min_max(lst):
    # Check if the list is empty
    if not lst:
        return None, None

    # Initialize min and max with the first element of the list
    min_val = max_val = lst[0]

    # Iterate through the rest of the elements
    for num in lst[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return min_val, max_val

# Ask user to enter array
user_input = input("Enter a list of numbers (seperated by space): ")
user_list = [int(x) for x in user_input.split()]

# Call the function with the user input
min_value, max_value = min_max(user_list)


# Print output
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")