# Assign a list using brackets, with elements separated by commas.
x = ["Now", "we", "are", "cooking", "with", 7, "ingredients"]

# Print element at index 3.
print(x[3])

# Trying to access an index not in list will result in IndexError.
#print(x[7])

# Access part of a list by slicing.
print(x[1:3])

# Omitting the first value of the slice implies a value of 0.
print(x[:2])

# Omitting the last value of the slice implies a value of len(list).
print(x[2:])

# Check the data type of an object using type() function.
print(type(x))

# The `in` keyword lets you check if a value is contained in the list.
x = ["Now", "we", "are", "cooking", "with", 7, "ingredients"]
print("This" in x)



# The append() method adds an element to the end of a list.
fruits = ['Pineapple', 'Banana', 'Apple', 'Melon']
fruits.append('Kiwi')
print(fruits)

# The insert() method adds an element to a list at the specified index.
fruits.insert(1, 'Orange')
print(fruits)

# The insert() method adds an element to a list at the specified index.
fruits.insert(0, 'Mango')
print(fruits)

# The remove() method deletes the first occurrence of an element in a list.
fruits.remove('Banana')
print(fruits)

# Trying to remove an element that doesn't exist results in an error.
# fruits.remove('Strawberry')
# print(fruits)

# The pop() method removes the element at a given index and returns it.
# If no index is given, it removes and returns the last element.
fruits.pop(2)
print(fruits)

# Reassign the element at a given index with a new value.
fruits[1] = 'Mango'

print(fruits)




# Strings are immutable because you need to reassign them to modify them.
power = '1.21'
power = power + ' gigawatts'
print(power)

# You cannot reassign a specific character within a string.
# power[0] = '2'

# Lists are mutable because you can overwrite their elements
power = [1.21, 'gigawatts']
power[0] = 2.21
print(power)