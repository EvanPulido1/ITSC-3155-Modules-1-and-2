# Evan Pulido
# ITSC 3155-151

# Empty list
list = []

# Ask the user to input ten numbers
number1 = int(input('Enter number 1: '))
number2 = int(input('Enter number 2: '))
number3 = int(input('Enter number 3: '))
number4 = int(input('Enter number 4: '))
number5 = int(input('Enter number 5: '))
number6 = int(input('Enter number 6: '))
number7 = int(input('Enter number 7: '))
number8 = int(input('Enter number 8: '))
number9 = int(input('Enter number 9: '))
number10 = int(input('Enter number 10: '))

# Put the numbers into a list
list.append(number1)
list.append(number2)
list.append(number3)
list.append(number4)
list.append(number5)
list.append(number6)
list.append(number7)
list.append(number8)
list.append(number9)
list.append(number10)

# print the list
print('Original list: ', list)

# Create a new list that contains the values that appear once
single_list = []

# A for loop that determines if a number is used more than once in the list
for x in list:
    number = x
    # Count command that checks list for duplicate numbers
    # if the number is not a duplicate then add it to a new list
    if list.count(number) < 2:
        single_list.append(number)

# Print the list that shows the numbers that only appear once
print('Numbers that appear once: ', single_list)

# The sources that I used are https://www.w3schools.com/python/ref_string_count.asp
# and previous exercises