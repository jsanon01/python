"""
I want a function 'usa'
I want a function 'capital of usa'
I want a function 'east side of usa'
I want a function 'west side of usa'
I want a function 'north side of usa'
I want a function 'south side of usa'

I want a main function to call all sub-functions: usa(), east(), west(), north(), south().
I want a while loop inside main function with the following info:
- usa() to be called when x = 1
- capital() to be called when x = 2
- east() to be called when x = 3
- west() to be called when x = 4
- north() to be called when x = 5
- south() to be called when x = 6

"""

def usa():
    print('USA stands for United States of America')

def capital():
    print('Washington D.C is the capital which is located on the East side')


def east():
    print('The East side faces Atlantic ocean')

def west():
        print('The West side faces Pacific ocean')

def north():
    print('The North side faces Canada')


def south():
    print('The South side faces Mexixo and Mediteranean sea.')

print('This script not only uses while-statement but also prints out sub-functions in a main loop.\n[0] Quit\t[1] USA\t\t[2] Capital\t[3] East\n[4] West\t[5] North\t[6] South')

def main():
    x = int(input('Enter a number from 0 - 6: '))

    while x:

        if x == 1:
            usa()
        elif x == 2:
            capital()
        elif x == 3:
            east()
        elif x == 4:
            west()
        elif x == 5:
            north()
        elif x == 6:
            south()
        else:
            print('Invalid entry...!')
        x = int(input('Enter a number from 0 - 6: '))

    print('You have exited the scipt...!')

main()

print()
