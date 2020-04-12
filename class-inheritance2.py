"""
I want to define a super-class named Parent
I want to define a function-method named parent
I want to define a sub-class named Child
I want to define a function-method named child
I want to instantiate an object
I want to call both methods: parent and child
"""


class Parent:
    def parent(self):
        print('\nThis a parent class --> class Parent: ')

class Child(Parent):
    def child(self):
        print('\nThis is a child class --> class Child(Parent):')


object = Child()
object.parent()
object.child()

print('\n--------------------------------------------')

class Karlo:
    def children(self):
        print('\nclass Karlo: Karo and Kris.')

class Roseline(Karlo):
    def child(self):
        print('\nclass Roseline(Karlo): Kerline aussi.')

enfants = Roseline()
enfants.children()
enfants.child()

print()
