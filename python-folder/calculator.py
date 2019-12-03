# This script prints out Calculator entries

print()

operations = input('Enter Add, Sub, Mul, or Div: ')

print('You choose to {}'.format(operations))

while True:

#    if operations.isdigit():

 #       break

    if operations == 'q':
 
       break

    number1 = int(input('Enter 1st number: '))

    number2 = int(input('Enter 2nd number: '))


    if operations == 'add':

        addition = number1 + number2

        print('{} + {} = {}'.format(number1, number2, addition))

    elif operations == 'sub':

        substraction = number1 - number2

        print('{} - {} = {}'.format(number1, number2, substraction))

    elif operations == 'mul':

        multiplication = number1 * number2

        print('{} * {} = {}'.format(number1, number2, multiplication))

    elif operations == 'div':

        division = number1 / number2

        print('{} / {} = {}'.format(number1, number2, division))

    else:

        print('Invalid number')

    operations = input("Enter Add, Sub, Mul, Div, or 'q' to exit!: ")

print()
