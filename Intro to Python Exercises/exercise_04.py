# Evan Pulido
# ITSC 3155-151

# Create an empty list
list = []

# Average of numbers in list
average = 0

# Ask the user to input a number
number = int(input('Enter a number: '))

# Take n floats from the user, store them in a list
x = range(number)
for n in x:
    new_number = float(input('Enter number ' + str(n + 1) + ': '))
    list.append(new_number)
    average = average + new_number

# Display the list
print('List:', list)

# Print the average of numbers in  list
print('Average: ' + str(average/number))

# I used exercise 3 to help with this problem and 
# https://www.w3schools.com/python/ref_list_append.asp