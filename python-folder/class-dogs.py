"""
I want to create a class named Dog
I want to create 1 global attribute
I want to create 2 instance level attributes

"""

class Dogs: # class dog created
    species = "'canine'" # global attribute
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

husky = Dogs('Sammi', 'Husky')

casey = Dogs('Casey','Chocolate Lab')

print('\nHere are the characteristics of the 2 dogs: ')

print('\n{} is a {}...'.format(husky.name, husky.breed))

print()

print("{} is a {}...".format(casey.name, casey.breed))

print('\nBoth dogs have {} as their species...'.format(casey.species.title()))

print()
