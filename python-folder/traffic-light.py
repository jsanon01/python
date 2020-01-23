from PIL import Image, ImageFilter

original = ''

original = Image.open('logo.png')

while True:
    
    color = input('\nEnter a color: ')

    if color == 'q':
        break

    elif color == 'red':
        print('COMPLETE STOP!')
    elif color == 'yellow':
        print('WARNING... Be Ready to Stop!')
    elif color == 'green':
        print('GO AHEAD!')
    elif color == 'open':
        original.show()
    else:
        print('Invalid entry...!')

print('Exited the loop')

print()
