# Write a function to convert a name into initials

# Ask user for input
name = input("Enter your full name:")

# Def function
def abbrev_name(name):
    words = name.split()

    initials = ".".join(word[0].upper() for word in words)

    return initials

print(abbrev_name(name))