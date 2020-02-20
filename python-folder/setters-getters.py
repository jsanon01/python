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

print('{} are good for vision...'.format(avocado.getName().title()))
