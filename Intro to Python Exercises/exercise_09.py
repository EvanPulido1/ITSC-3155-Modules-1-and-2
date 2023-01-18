# Evan Pulido
# ITSC 3155-151

# Ask the user to input five words
word1 = str(input('Enter a word: '))
word2 = str(input('Enter a word: '))
word3 = str(input('Enter a word: '))
word4 = str(input('Enter a word: '))
word5 = str(input('Enter a word: '))

# Add the words into a list
list = []

list.append(word1)
list.append(word2)
list.append(word3)
list.append(word4)
list.append(word5)

# Print the list
print('Words: ', list)

# Create an empty string
empty_string = ''

# Use a for loop to iterate through the list and add each word
# to the string with a space in between them
for x in list:
    empty_string += x + ' '

# print the string with the words combined
print('One string: ' + empty_string)

# I used previous exercises and their links for this exercise