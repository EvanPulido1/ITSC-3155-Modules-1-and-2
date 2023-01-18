# Evan Pulido
# ITSC 3155-151

# Asking for user input
word1 = input('Enter a string: ')
word2 = input('Enter another string: ')

# An if elif statement that makes it so shortest word is the suffix
# to allow for the command 'endswith' to work

# The 'len' command tells the length of the given string
# The 'endswith' command returns true if string has suffix
# and false if it does not
if (len(word1) > len(word2)):
    suffix = word1.endswith(word2)
    print(suffix)
elif (len(word2) > len(word1)):
    suffix = word2.endswith(word1)
    print(suffix)

# My sources that helped me are https://www.programiz.com/python-programming/methods/string/endswith
# and https://www.w3schools.com/python/ref_func_lens.asp