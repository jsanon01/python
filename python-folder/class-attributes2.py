"""
I want to define a class named 'Car'
I want to define 2 attributes inside 'Car'
I want to print these attributes
-----------------------------------------
I want to define a class named 'Humans'
I want to define 3 attributes inside 'Huamns'
I want to print these attributes

"""

print("\nThis script prints out 2 attributes of 'class Car': color and sound.")

class Car():

    door = '4 doors' # sound attribute

    color = 'red' # color attribite

datsun = Car()

datsun.door = '6 doors' # MODIFIED

print("\nThis Datsun has the following characteristics:\n'{}' color and '{}'".format(datsun.color, datsun.door)) # accessing object attribute with dot (.) syntax COLLECTIVELY

#print('\nThe color of this Datsun is: {}'.format(datsun.color)) # accessing object attribute with dot (.) syntax INDIVIDUALLY

print('\nThe MODIFIED Datsun door is: {}'.format(datsun.door)) # accessing object attribute wit dot (.) syntax INDIVIDUALLY

print()

"""
print('-------------------------------------------------------------------------')

print("\nThis script prints out 3 attributes of 'class Humans':\nlife, nerves, and eyes.")

class Humans():
    bio = 'bios\t => means life and logy => study'
    neu = 'neuro\t => means nerves and logy => study'
    oph = 'ophtha => means eyes and logy => study'

person = Humans()

print('\nHere are some of the Human studies related to Ancient Greek:\n- {}\n- {}\n- {} '.format(person.bio, person.neu, person.oph)) # accessing 3 object attributes with dot (.) syntax COLLECTIVELY

print()
"""
