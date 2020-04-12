


class Parent:
    def parent(self):
        print('\nThis a parent class')

class Child(Parent):
    def child(self):
        print('\nThis is a child class')

#object = Parent()
#object.parent()

object = Child()
object.parent()
object.child()
print('\n--------------------------------------------')

class Karlo:
    def children(self):
        print('\nKaro and Kris')

class Roseline(Karlo):
    def child(self):
        print('\nKerline aussi')

enfants = Roseline()
enfants.children()
enfants.child()
print()
