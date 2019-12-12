# This script checks if 2 numbers are equal to 100


print('This script checks if 2 numbers are equal to 100')

number = ''

while number != 'q':

    number1 = int(input('Enter 1st number: '))

    number2 = int(input('Enter 2nd number: '))

    total = number1 + number2

    print('The total is: {} + {} = {}'.format(number1, number2, total))

    if total == 100:

        print('Congratulations, You entered 2 right numbers!')

    else:

        print('Keep trying...! You entered 2 wrong numbers...!')

        number = input("Press 'Enter' to continue or 'q' to exit the loop!: ")

print('You have exited the loop!')
