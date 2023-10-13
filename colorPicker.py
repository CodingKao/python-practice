# Create a blank list called colors
colors = []

# Define a function 'get_color' which prompts the user for a 'color' and returns it
def get_color():
    color = input('Please enter a color to add it to the list or enter "done" to exit: ')
    return color

# Begin the REPL
while True:
    # Call the get_color() function to get a color from the user
    color = get_color()

    # If the user enters 'done' instead of a color, display the list of colors to the user and exit the loop
    if color == 'done':
        # Display the colors using .join() to place a comma and a space between each color
        print(f"The colors you entered were: {', '.join(colors)}")
        # End the loop
        break

    # If the color is already in the colors list, inform the user that the color is already in the list and repeat the loop
    if color in colors:
        print(f'The color {color} is already in the list!')
        continue

    # If the color is not already in the colors list, add it and tell the user it was added.
    print(f'The color {color} was added to the list!')
    colors.append(color)
