# Return String
# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".


# Get the name from the user
name = input("Please enter your name:")

# Define the greeting function
def greeting(name):
    return f"Hello, {name} how are you doing today?"

# Print the greeting message
print(greeting(name))