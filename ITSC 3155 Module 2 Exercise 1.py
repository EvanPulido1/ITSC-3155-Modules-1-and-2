# Evan Pulido
# ITSC 3155-151

# Ask the user to enter a string
word = input('Enter a string: ')

# Create an empty string that will be holding the reversed string
empty_string = ''

# A for loop that iterates through the word given and makes a string with the letters in the word reversed
for x in word:
    empty_string = x + empty_string

# Print the string provided in reverse
print(empty_string)