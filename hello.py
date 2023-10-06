print("hello world!")

# Ouput "Hello world!"

# the letters of a word, each in its own string
print('P'+'y'+'t'+'h'+'o'+'n')

# the individual words of a sentence.  
# Place spaces betwee each word
# using separate strings
print("Python"+" "+"is"+" "+"fun")

# the individual characters in a sentence,
# including spaces and punctuation.
# each and every character should be its own string.
print('H'+'e'+'l'+'l'+'o'+' '
+'w'+'o'+'r'+'l'+'d'+'.'+' '
+'P'+'y'+'t'+'h'+'o'+'n'+' '
+'i'+'s'+' '
+'f'+'u'+'n'+'.')


# Multi-line comment:
'''
-.-'*'-.-'*
   Project: Python
   Version: 1.0
   Date: Oct, 2023
'-.-'*'-.-'*'-.-'*'-.-'*
'''

# Single lines:

print("*'-.-'*'-.-'*'-.-'*'-.-'*")
print("     Project: Python")
print("     Author: Kao")
print("     Date: Oct, 2023")
print("*'-.-'*'-.-'*'-.-'*'-.-'*")


# Multi-line

print('''
        *'-.-'*'-.-'*'-.-'*'-.-'*
            Project: Python
            Version: 1.0
            Author:  Kao
            Date: Oct, 2023
        *'-.-'*'-.-'*'-.-'*'-.-'*
        '''        
)


print("The time has come,' the Walrus said,")  # line 1
# print("'Twas brillig, and the slithy toves")
print("To talk of many things:")  # line 2
# print("Did gyre and gimble in the wabe:")
print("Of shoes — and ships — and sealing-wax —")  # line 3
# print("All mimsy were the borogoves, ")
print("Of cabbages — and kings —")  # line 4
# print("And the mome raths outgrabe. ")
print("And why the sea is boiling hot —")  # line 5
# print("O frabjous day! Callooh! Callay!")
print("And whether pigs have wings.'")  # line 6

# capitalize a word
word = input('Enter a word: ')
print(word.capitalize())

# display a word in all capital letters and all lowercase letters
#print in all upper case
print(word.upper())

#print in all lowercase
print(word.lower())

# exchange all instances of a letter within a word with a different
#mizzizzippi
print('mizzizzippi'.replace('z','s'))