"""
I want to call PIL from library
I want to open an image named 'logo.png'
I want to use a while statement for the 3 colors: red, yellow, and green

"""
from PIL import Image, ImageFilter

original = ''

original = Image.open('logo.png')

print("\nThis script prints out the following:\n[red]  [yellow]  [green]  ['open' an image]  ['q' for Quit]")

while True:
    
    color = input('\nEnter a color: ')

    if color == 'q':
        break

    elif color == 'red':
        print('Red leads to a complete STOP!')
    elif color == 'yellow':
        print('WARNING... Be Ready to Stop!')
    elif color == 'green':
        print('Green means Go...GO AHEAD!')
    elif color == 'open':
        original.show()
    else:
        print('Invalid entry...!')

print('You have exited the loop...')

print()
