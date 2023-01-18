# Evan Pulido
# ITSC 3155-151

# Create an empty list
list1 = []
list2 = []

# Ask user to input numbers
number1 = int(input('Enter a number for the first list: '))
number2 = int(input('Enter a number for the first list: '))
number3 = int(input('Enter a number for the first list: '))
number4 = int(input('Enter a number for the first list: '))
number5 = int(input('Enter a number for the first list: '))

# Add numbers to first list
list1.append(number1)
list1.append(number2)
list1.append(number3)
list1.append(number4)
list1.append(number5)

# Ask user to input more numbers
number6 = int(input('Enter a number for the second list: '))
number7 = int(input('Enter a number for the second list: '))
number8 = int(input('Enter a number for the second list: '))
number9 = int(input('Enter a number for the second list: '))
number10 = int(input('Enter a number for the second list: '))

# Add numbers to second list
list2.append(number6)
list2.append(number7)
list2.append(number8)
list2.append(number9)
list2.append(number10)

# Use the set command which allows you to check specific elements
x = set(list1)
y = set(list2)

# display the lists
print('First list:', list1)
print('Second list:', list2)

# If there is a common numbers between the two lists 
# have another list displaying the numbers
if (x & y):
    print('Third list:', list(x & y))

# I used https://www.geeksforgeeks.org/sets-in-python/ to help me 
# I also used the previous exercises to help with this one