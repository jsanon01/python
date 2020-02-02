"""
I want to define a class named 'Car'
I want to define 2 attributes inside 'Car'
I want to print these attributes

"""

print("\nThis script prints out 2 attributes of 'class Car': color and sound.")

class Car():

    door = '4 doors' # sound attribute

    color = 'red' # color attribite

datsun = Car()

print('\nThis Datsun has the following characteristics: {} color and {}'.format(datsun.color, datsun.door)) # accessing object attribute with dot (.) syntax COLLECTIVELY

#print('\nThe color of this Datsun is: {}'.format(datsun.color)) # accessing object attribute with dot (.) syntax INDIVIDUALLY

#print('\nThe sound of this Datsun is: {}'.format(datsun.sound)) # accessing object attribute wit dot (.) syntax INDIVIDUALLY

print()

"""
class Humans():
    bio = 'bios = life and logy = study'
    neuro = 'neuro  = nerves and logy = study'
    ophtha = 'ophtha  = eyes and logy = study'

john = Humans()

print(john.bio)

"""
