

num1 = ''

num2 = ''
add = ''
sub = ''

choice = input('Please enter: Add, Sub, Mul, and Div.\nEnter your choice: ')
print('Your choice is: {}'.format(choice))


"""
if choice == 'add':
    print('Addition: {}'.format(addNumbers()))
else:
    print('Substraction: {}'.format(addSub))

"""

def addNumbers(num1, num2):
    num1 = int(input('Enter 1st number: '))
    num2 = int(input('Enter 2nd number: '))
    result = num1 + num2
    print('{} + {} = {}'.format(num1, num2, result))

addNumbers(num1, num2)


def subNumbers(num1, num2):
    num1 = int(input('Enter number: '))
    num2 = int(input('Enter number: '))
    result = num1 - num2
    print('{} - {} = {}'.format(num1, num2, result))
    
subNumbers(num1, num2)

def mulNumbers(num1, num2):
    num1 = int(input('Enter number: '))
    num2 = int(input('Enter number: '))
    result = num1 * num2
    print('{} * {} = {}'.format(num1, num2, result))

mulNumbers(num1, num2)



def divNumbers(num1, num2):
    num1 = int(input('Enter number: '))
    num2 = int(input('Enter number: '))
    result = num1 / num2
    print('{} / {} = {}'.format(num1, num2, result))

divNumbers(num1, num2)
    

