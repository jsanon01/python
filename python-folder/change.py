# This script prints the amount of change you entered

change = 'Enter the amount of coins to calculate'

while change != 'q':

    change = print('Enter the amount of coins to calculate:')

    quarter = int(input('Enter quarters: '))

    nickel = int(input('Enter nickels: '))

    dime = int(input('Enter dimes: '))

    pennies = int(input('Enter pennies: '))

    total = .25*quarter + .10*dime + .05*nickel + .01*pennies

    print(f'The total value of your change is: ${total}')

    change = 'Enter the amount of coins to calculate'

print('You have exited the loop!')
