# Evan Pulido
# ITSC 3155-151

# I used https://www.geeksforgeeks.org/how-to-take-integer-input-in-python/ to help me
# learn how to ask for user input
grade = int(input('Enter your grade from 0 to 100: '))

# I used https://www.programiz.com/python-programming/if-elif-else to help me
# learn how to use if elif statements
if grade >= 0 and grade < 60:
    print('Your grade is F')
elif grade >= 60 and grade < 70:
    print('Your grade is D')
elif grade >= 70 and grade < 80:
    print('Your grade is C')
elif grade >= 80 and grade < 90:
    print('Your grade is B')
elif grade >= 90 and grade <= 100:
    print('Your grade is A')