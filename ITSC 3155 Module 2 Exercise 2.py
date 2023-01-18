# Evan Pulido
# ITSC 3155-151

# Ask the user to enter a string 
word = input("Enter a string: ")

# Get the length of the string provided and add it to a variable
# I used https://realpython.com/len-python-function/#:~:text=The%20function%20len()%20is,valid%20arguments%20for%20len()%20.
# this link to help me learn and understand the len command which gives the length of the provided string
word_length = len(word)

# Create two empty strings that will hold the upper and lower case letters from the string
upper_case_letters = ''
lower_case_letters = ''

# A for loop that uses the range command to iterate the number of times that the string has letters
# https://www.w3schools.com/python/ref_func_range.asp
for x in range(0, word_length, 1):
    letters = word[x]

    # An if else statement that determines if the letters from the string are upper or lower case
    if (letters >= 'A' and letters <= 'Z'):
        # If the letters are in upper case then add it to the upper_case_letters
        upper_case_letters = upper_case_letters + letters
    else:
        # Otherwise the letters in the lower case are added it to the lower_case_letters
        lower_case_letters = lower_case_letters + letters

# Create a variable that holds the lower and upper case letters together
new_word = lower_case_letters + upper_case_letters

# A variable that replaces the spaces in the string with no spaces
# Link that helped me understand this command is https://www.w3schools.com/python/ref_string_replace.asp
newer_word = new_word.replace(' ', '')

# Print the new string with the lower case letters first and upper case letters last, all with no spaces
print(newer_word)

# The other website that I used as a source is https://www.geeksforgeeks.org/move-all-uppercase-char-to-the-end-of-string/
