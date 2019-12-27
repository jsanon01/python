# This script returns 2 names in a function

print()

first, last = '  '

print('This script returns 2 names in a function:\n')

def fullName(first, last):

    first = input('Enter first name: ')

    last = input('Enter last name: ')

    return first, last


names = fullName(first, last)

print('You have entered: {}'.format(names).title())

print()
