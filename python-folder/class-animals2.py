"""
I want to create a class named Animals
I want to create a class attribute named species
I want to create setter and getter to access attribute value

I want to define a main loop
I want to create an instance called lion
I want to call the setter method with feline as argument
I want to print out species by calling getter method
"""

class Animals:
    def __init__(self, species):
        self.species = species

    def setAnimal(self, species):
        self.species = species

    def getAnimal(self):
        return self.species

species = ''

def main():
    lion = Animals(species)
    lion.setAnimal('le lion de la tribu de juda'.upper())
    print(lion.getAnimal().title())

main()
