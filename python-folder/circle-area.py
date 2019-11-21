# This script prints a circle-radius area using Math function
import math


radius = ''

while radius != 0:

    radius = int(input('Enter a number: '))

    def circle_area(radius):
        return math.pi * radius ** 2

    area = circle_area(radius)

    print(f'The value of the circle area is: {area}')

print('You have exited the loop!')
