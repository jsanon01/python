# This script has 4 options:
# 1) open image 2) displays image size 3) resize image 4) rotate image

# importing the libraries
from PIL import Image

# print statemnt greeting
print("\nThis script displays 4 options about an image:\n[open image]\t[display size image]\t[rotate image]\t[resize image]")

# I ask the user what to do: open, size, resize, rotate, or quit
option = input("\nWhat do you want to do with the image?\n[open]\t\t[size]\t\t[resize]\t[rotate] or 'q'to exit: ")

# user interaction or response of the printing statement
print("\nYou choose to {} the image".format(option))

# I assign while loop
while True:

    # I assign if statement to break or exit the loop
    if option == 'q':
        break

    # I use if statement to open image
    if option == 'open':
        image = Image.open(input('\nEnter image you would like to open: '))
        image.show()


    # I use elif statement to get actual size of the image
    elif option == 'size':
        image = Image.open(input('\nEnter image to get actual size: '))
        print("\nThe actual size of image is expressed in format (width, length): ",image.size)

    # I use elif statement to open an existing image
    elif option == 'resize':
        image = Image.open(input('\nEnter existing image: '))

        # I use parameters after opening existing image
        width = int(input('\nEnter width: '))
        length = int(input('\nEnter length: '))
        size=(width, length)
        # image resizing
        output = image.resize(size)
        # image saved with a different name
        output.save(input('\nEnter name of image to be saved: '))
        # image to display on screen
        output.show()

    # I use elif statement to rotate an existing image
    elif option == 'rotate':
        image = Image.open(input('\nEnter image to rotate: '))

        # I use integer to rotate the angle
        angle = int(input('\nEnter the angle: '))
        output = image.rotate(angle)
        # I save image with a new filename
        output.save(input('\nEnter name of image to save: '))

    # I use else statement for invalid path or characters
    else:
         print('\nInvalid path or characters')

    # I insert the condition to iterate the loop
    option = input("\nWhat do you want to do with the image?\n[open]\t\t[size]\t\t[resize]\t[rotate]\t or 'q' to exit: ")


print()
