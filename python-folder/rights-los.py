"""
I want to define a function called life
I want to define a function called ownership
I want to define a function called speech

I want to define a main function

The main function will have a while statement with the following conditions:
- life will be called when x = 1
- ownership will be called when x = 2
- speech will be called when x = 3

"""


def life():
    print("\nhuman lives don't matter when ignorance exist..")

def ownership():
    print('\nownership is worthless when lack of information prevails')

def speech():
    print('\nspeech is cheap when unawareness triumph')

print('\nThis script prints out 3 functions and a main function.')

print('\n[0] Quit\t[1] Life\t[2] Ownership\t[3] Speech')

def main():
    x = int(input('\nEnter a number from 0 - 3: '))
    while x:
        if x == 1:
            life()
        elif x == 2:
            ownership()
        elif x == 3:
            speech()
        else:
            print('Invalid number...')

        x = int(input('\nEnter a number from 0 - 3: '))

main()

print('\nExiting the script')

print()
