"""
I want to define a class named Dog
I want to define a setter inside the class named Dog
I want to define a getter inside the class named Dog
I want to print out the return value

"""

class Dog:

    name = ''

    def setName(self, new_name):
        self.name = new_name # declaring new value for name attribute

    def getName(self): # returning value of name attribute
        return self.name

print('\nThis script prints out setters and getters from a class.')

sam = Dog()

sam.setName("gregory toussaint")

print('\nTabernacle De Gloire: {}'.format(sam.getName().title()))

print()
