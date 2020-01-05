"""
I want a function to print a message 'Senateur du Sud'
I want a function to print a message 'Senateur de Jeremie'
I want a function to print a message 'Senateur de Jacmel'
I want a main function to call: sud(), jeremie(), jacmel()

I want sud function to be called when x = 1
I want sud function to be called when x = 2
I want sud function to be called when x = 3

I want to call the main function
"""
print('\nThis script prints 3 separate functions when being asked.')

def sud():
    print('Senateur du Sud')

def jeremie():
    print('Senateur de Jeremie')

def jacmel():
    print('Senateur de Jacmel')

def main():
    x = int(input('Enter a number: '))
    while x:

        if x == 1:
            sud()
        elif x == 2:
            jeremie()
        elif x == 3:
            jacmel()
        else:
            print('Invalid Number.')
        x = int(input('Enter a number: '))

    print('\nYou have exited the script!')


main()
