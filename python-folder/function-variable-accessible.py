# This script prints out an accessible variable inside a function

print()

print('This script prints out an accessible variable inside a function.')

def function():

    word = 'makaron' # accessible variable

    return word

value = function()

print('\nThe accessible variable inside the function is named: {}'.format(value))

print()
