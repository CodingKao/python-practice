# Create a dictionary of fruits. The 'name' of each 'fruit' will be the key and value will be its 'price'
fruits = {
    'apple': 0.65,
    'banana': 0.5,
    'guava': 0.33
}

# Display the price of a fruit
print(f"Apples cost ${fruits['apple']} each.")

# Add 'grapes'
fruits['grapes'] = 0.99
print(f"Added 'grapes': {fruits}")

# Remove a fruit from the dictionary
# Print the dictionary to verify its deletion

# Delete the key: value pair for 'banana'
del fruits['banana']
print(f"Removed 'banana': {fruits}")

# Loop through the dictionary and display each item and its price
print('   Fruits   ')
print('------------')

for fruit, price in fruits.items():
    print(f'{fruit}: ${price}')

'''
Create another dictionary to represent a shopping_basket.
The keys of this dictionary will be fruit names and 
the values will be the quantity of each item in the shopping_basket.
Loop through the shopping_basket and add up the grand_total. 
With each iteration of the loop, also print out how 
many of each fruit is in the shopping_basket and the sub_total for that fruit.
Display all the sub_totals and the grand_total to look like a receipt in the terminal
'''

# Fruits and their prices per item
fruit_prices = {
    'apple': 0.65,
    'banana': 0.5,
    'guava': 0.33,
}

# Fruits in the basket and their quantities
shopping_basket = {
    'apple': 4,
    'banana': 6,
    'guava': 8,
}

# Set the grand_total to zero
grand_total = 0

for fruit, quantity in shopping_basket.items():
    # Calculate the sub_total for the current fruit
    sub_total = quantity * fruit_prices[fruit]

    # Add the sub_total for the current fruit to the grand total
    grand_total += sub_total

    # Print the sub_total for the current fruit
    print(f'{quantity} {fruit.capitalize()}s: ${sub_total}')

print('----------------')
print(f'Grand Total: ${grand_total}')
