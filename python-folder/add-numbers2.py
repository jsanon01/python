# This script prints operations using functions

num1 = ''

num2 = ''

add = ''

sub = ''

#choice = input('Please enter: Add, Sub, Mul, and Div.\nEnter your choice: ')
#print('Your choice is: {}'.format(choice))


"""
if choice == 'add':
    print('Addition: {}'.format(addNumbers()))
else:
    print('Substraction: {}'.format(addSub))

"""
#print('This script simultaneously prints out the following operations: Add, Sub, Mul, and Div.\nPlease enter 2 numbers: ')

num1 = int(input('Enter 1st number: '))

num2 = int(input('Enter 2nd number: '))


def addNumbers(num1, num2):
    result = num1 + num2
    print('Addition: {} + {} = {}'.format(num1, num2, result))

addNumbers(num1, num2)


def subNumbers(num1, num2):
    result = num1 - num2
    print('Substraction: {} - {} = {}'.format(num1, num2, result))
    
subNumbers(num1, num2)


def mulNumbers(num1, num2):
    result = num1 * num2
    print('Multiplication: {} * {} = {}'.format(num1, num2, result))

mulNumbers(num1, num2)



def divNumbers(num1, num2):
    result = num1 / num2
    print('Division: {} / {} = {}'.format(num1, num2, result))

divNumbers(num1, num2)
    

