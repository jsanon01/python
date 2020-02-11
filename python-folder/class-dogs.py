"""
I want to create a class named Dog
I want to create 1 global attribute
I want to create 2 instance level attributes

"""

class Dogs: # class dog created
    species = 'caninie' # global attribute
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

husky = Dogs('Sammi', 'Husky')

casey = Dogs('Casey','Chocolate Lab')

print('\nHere are the characteristics of the 2 dogs: ')

print('\n{} {}'.format(husky.name, husky.breed))

print("{} {}".format(casey.name, casey.breed))

print()
