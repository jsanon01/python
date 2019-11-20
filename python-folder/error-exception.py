# This script prints error exception

number = ''

while number != 'q':
    
    a = int(input('Enter 1st number: '))

    b = int(input('Enter 2nd number: '))

    try:
        print(a/b)
    except ZeroDivisionError:
        print('b can not be zero. Try again.')
    
