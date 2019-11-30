# This script prints 3 colors with points accordingly

alien = print('Enter one of the followong colors: green, yellow, and red...')

alien_color = input("Enter a color: ")

while alien_color != 'q':
    if alien_color == 'green':
        print("You have earned 5 points.")
    elif alien_color  == 'yellow':
        print("You have earned 10 points.")
    elif alien_color == 'red':
        print("You have earned 15 points.")
    else:
        print("No color matchs your request!")
    alien_color = input("Enter a color: ")
    aliens = 'Enter q to quit: '

print('You have exited the loop!')

