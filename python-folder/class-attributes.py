"""
I want to define a class named 'Car'
I want to define 2 attributes inside 'Car'
I want to print these attributes

"""

print("\nThis script prints out 2 attributes of 'class Car': color and sound.")

class Car():
    sound = 'beep, beep' # sound attribute

    color = 'red' # color attribite

datsun = Car()

print('\nThe color of this Datsun is: {}'.format(datsun.color))

print('\nThe sound of this Datsun is: {}'.format(datsun.sound))

print()
