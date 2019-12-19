# This script not only asks for inputs from user but also prints them as: Add, Sub, Mul, and Div.


print()

print('This script not only asks for inputs from user but also prints them as: Add, Sub, Mul, and Div.')

def calculation():
    print()
    x = int(input('Enter 1st input: '))
    print()
    y = int(input('Enter 2nd input: '))
    print()
    print('Addition: {} + {} = {} '.format(x, y, x+y ))
    print()
    print('Substraction: {} - {} = {} '.format(x, y, x-y ))
    print()
    print('Multiplication: {} * {} = {} '.format(x, y, x*y ))
    print()
    print('Division: {} / {} = {} '.format(x, y, y/x ))


calculation()

print()
