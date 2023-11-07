def closest_to_zero(lst):
    if not lst:
        return None  # Return None for an empty list

    # Find the element with the minimum absolute difference from zero
    closest_value = min(lst, key=lambda x: abs(x))

    # Check if there is more than one element with the same absolute difference
    if lst.count(closest_value) > 1:
        return None  # Return None if not possible to define only one closest value
    else:
        return closest_value

# User Input:
input_numbers = input("Enter a list of numbers separated by spaces: ")

# Convert the input string to a list of integers
numbers = [int(num) for num in input_numbers.split()]

result = closest_to_zero(numbers)
print(result)
