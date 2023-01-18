# Evan Pulido
# ITSC 3155-151

# Ask the user to input the first number
character = input('Enter a number or QUIT to quit: ')

# This is an empty list
list = []
even_list = []

# Add the first number to the list
list.append(int(character))

# A while loop that iterates until the user inputs QUIT
while character != 'QUIT':
    # Ask for user input
    character1 = input('Enter a number or QUIT to quit: ')
    # If the value inputted is equal to QUIT then the loop breaks
    if character1 == 'QUIT':
        break
    # Add the values into the list
    list.append(int(character1))

    # If the number that user inputted is even then add to a separate list
    if (int(character1) % 2) == 0:
        even_list.append(int(character1))

# Print the lists with all the numbers inputted by the user
print('All numbers: ', list)

# Print a new list with even numbers from the other list
print('Even numbers: ', even_list)

# The sources that I used to help me solve this are
# https://www.toppr.com/guides/python-guide/examples/python-examples/python-program-to-check-if-a-number-is-odd-or-even/#.~:text=The%20required%20code%20is%20provided%20below.&text=num%20%3D%20int%20(input%20(%E2%80%9C,even%3A%20887%20887%20is%20odd.
# and https://www.w3schools.com/python/python_while_loops.asp