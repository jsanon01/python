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
    print('The East side is facing Atlantic ocean')

def west():
        print('The West side is facing Pacific ocean')

def north():
    print('The North side is facing Canada')


def south():
    print('The South side is facing Mexixo and Mediteranean sea.')


def main():
    x = int(input('Enter input: '))

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
        x = int(input('Enter input: '))

    print('You have exited the scipt...!')

main()

print()
