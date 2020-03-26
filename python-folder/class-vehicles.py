"""
I want to define a class named Vehicle
I want to define a class variable named 'name'
I want to define a class variable named 'kind'
I want to define a class variable named 'color'
I want to define a class variable named 'value'

"""


class Vehicle:
    # defining class variables
    name = 'bmw'.upper()
    kind = 'convertible'.title()
    color = 'red'.title()
    value = 100000.00

car1 = Vehicle()
# instance variables in 1 line
print('\nHere is the spec:\n{} {} {} {}\n '.format(car1.name, car1.kind, car1.color, car1.value))
#print()
