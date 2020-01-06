# This script prints the Perimeter of a rectangle

print()

print('This script prints the Perimeter of a rectangle.')

print('Units are usually measured in Sq Ft, Inch, or Meter...')

length = int(input('Enter the value of the Length: '))

width = int(input('Enter the value of the Width: '))

perimeter = 2 * (length + width)

print('The perimeter of this rectangle is: 2 x ({} + {}): Perimeter = {}'.format(length, width, perimeter))

print()
