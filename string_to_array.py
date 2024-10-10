# Write a function to split a string and convert it into an array of words.

# define the function
def string_to_array(s, delimiter=" "):
    return s.split(delimiter)

# example usage / ask user for input
input_string = input("Enter a string: ")

# Call the function and print result
word_array = string_to_array(input_string, ",")
print(word_array)