# Sing Happy birthday to user

# Ask user for their name
name = input("Enter your name: ")

# Methond 1 strings
print("Person one")
print("Happy birthday to you!")
print("Happy birthday to you!")
print(f"Happy birthday dear {name}!")
print("Happy birthday to you!")

# Method 2 functions
def happy_birthday(name):
    print("Person two")
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print(f"Happy birthday dear {name}!")
    print("Happy birthday to you!")

happy_birthday(name)