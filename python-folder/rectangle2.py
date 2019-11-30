# This script prints a rectangle with rows and columns using For-Loop

print()

rows = int(input('Enter number of rows: '))

columns = int(input('Enter number of columns: '))

character = input('Enter a character: ')

print()

for i in range(rows):

    for j in range(columns):

        if (i == 0 or i == rows -1 or j == 0 or j == columns -1):

            print('%c' %character, end = ' ') 

        else:

            print(' ', end = ' ')

    print()

print()
