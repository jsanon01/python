# This functions sets default parameter values (as optional)


print('This functions sets default parameter values.\n(where middle name is optional)')

def printName(first, last, middle=" "):

    if middle:

        print('{} {} {}'.format(first, last, middle))

    else:

        print('{} {}'.format(first, last))

printName('Jean', 'Max', 'Paul')

printName('Jean', 'Max')
