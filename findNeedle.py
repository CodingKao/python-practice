# A Needle in the Haystack

# Define the function
def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'

# Example
hay_array = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]

# call the function
result_output = find_needle(hay_array)

# print result
print(result_output)