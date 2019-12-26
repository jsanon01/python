# This script not only passes 2 inputs and prints out "No Name passed in" otherwise.'


fname, lname = "  "

print()

print('This script not only passes 2 inputs (first name & last name)\nbut also it prints out "No Name passed in" otherwise.')

print()

def function(fname = ' ', lname=" "):

    fname = input('Enter first name: ')

    lname = input('Enter last name: ')

    if fname:

        print('You entered: {} {}'.format(fname, lname).title())

    elif lname:

        print('You entered: {} {}'.format(fname, lname).title())

    else:

        print('No name passed in.')


function(fname, lname)

print()
