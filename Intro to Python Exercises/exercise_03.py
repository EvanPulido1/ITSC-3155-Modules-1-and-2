# Evan Pulido
# ITSC 3155-151

# Ask the user to input a number and make sure
# number is bigger than 1
number = int(input('Enter an integer greater than 1: '))

# Printing the cubes of each integer from 0 to the inputted integer
x = range(number)
for n in x:
    print('The cube of ' + str(n) + ' is ' + str(n * n))
print('The cube of ' + str(number) + ' is ' + str(number * number))

# The link that I used to help me solve this assignment is
# https://www.w3schools.com/python/ref_func_range.asp