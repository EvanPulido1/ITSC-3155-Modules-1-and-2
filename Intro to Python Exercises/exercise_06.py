# Evan Pulido
# ITSC 3155-151

# Create an array
zero_array = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# Ask the user to enter a row number and column number
row = int(input('Enter a row number from 1 to 5: '))
column = int(input('Enter a column number from 1 to 5: '))

# insert 1 into given row and column
zero_array[row][column] = 1

# Print array using two for loops with the first for loop iterting the outer array
for x in zero_array:
    for y in x:
        print(y, end=' ')
    print()

# The resources I used to help me with this is 
# https://www.scaler.com/topics/2d-array-in-python/
# https://www.toppr.com/guides/python-guide/questions/what-does-end-do-in-python/
# https://www.tutorialspoint.com/python_data_structure/python_2darray.htm