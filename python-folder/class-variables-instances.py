"""
I want to define a class named Shark
I want to define a construct method with 2 instance variables: name and age
I want to define a class method named jeremie
I want to instantiate the variables

I want to print all the instance variables in one line
"""

# defining a class
class Shark:
    
    # defining construct method with 2 instance variables
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # defining a method named jeremie with instance variable named location
    def jeremie(self, location):
        self.location = location

# Instantiating meaning assigning piskette as instance
piskette = Shark('piskette', 9)

# printing out 2 instance varaibles
print('\nthe object: piskette = passes the parameters --> {} and {}'.format(piskette.name, piskette.age))

# Instantiating meaning assigning sou_fort as instance
sou_fort = Shark("'La Pointe'",250)

# printing out 2 instance variables
print('\nthe object: sou_fort = passes the parameters --> {} and {}'.format(sou_fort.name, sou_fort.age))

print()
