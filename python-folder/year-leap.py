# This script checks out if it is a Leap Year or not

print()

year = ""

print('This script checks out if it is a Leap Year or not')

while year != 'q':

    year = input('Enter a year number or q to quit: ')

    if year.isdigit(): # '1'.digit() 'w'.isdigit() 'karlo'.isdigit()

        year = int(year) # year = int('1')

        if year % 4 == 0:

            print('Yes {} is a leap year...!'.format(year))

        else:

            print('No {} is not a leap year!'.format(year))

print()
