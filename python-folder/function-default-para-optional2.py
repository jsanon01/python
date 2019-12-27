# This functions sets default parameter values (as optional)

print()

print('This functions sets default parameter values.\n(where middle name is optional)')

first, last, middle = '   '

def printName(first, last, middle=" "):

    first = input('Enter first name: ')

    middle = input('Enter middle name: ')

    last = input('Enter last name: ')

    if middle:

        print('You entered: {} {} {}'.format(first, middle, last).title())

    else:

        print('You entered: {} {}'.format(first, last).title())


printName(first, last, middle)

print()
