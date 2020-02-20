"""
I want to define a class named Veggies
I want to define a setter inside the class named Veggies
I want to define a getter inside the class named Veggies
I want to print out the return valuedefine a class named Veggies

"""

class Veggies:
    name = ''
    def setName(self, carrots):
        self.name = carrots

    def getName(self):
        return self.name

avocado = Veggies()

avocado.setName('carrots')

print('\nThis script prints out setters and getters from a class')

print('\nHaving carotene, {} are not only good for vision\nbut also for pigmentation.'.format(avocado.getName().title()))

print()

print('-------------------------------------------------------------')

class Vitamins:
    vitamin = ''
    def setVitae(self, b_12):
        self.vitamin = b_12
    def getVitae(self):
        return self.vitamin

vitamin_e = Vitamins()

vitamin_e.setVitae('vitamin b-12')

print('\nThis script prints out setters and getters from a class')

print('\n{} is a water soluble vitamin\nthat is naturally present in some foods'.format(vitamin_e.getVitae().title()))

print()
