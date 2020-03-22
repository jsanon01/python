"""
I want to define a parent class named Fish
I want to define __init__ method with first_name and last_name
I want to define another method named swim()
I want to define a child class named swim_backwards()

I want to define a child class named Trout() or object
I want to create a Trout object named terry that will use Fish class
"""

class Fish:
    def __init__(self, first_name, last_name='Fish'):
        self.first_name = first_name
        self.last_name = last_name

    def swim(self):
        print('\nthe fish swims smoothly...'.title())

    def swim_backwards(self):
        print('\nall fish can swim backwards...'.upper())



class Trout(Fish):
    pass

print()

terry = Trout('terry'.title())

print(terry.first_name, terry.last_name)

#print(terry.first_name + ' ' + terry.last_name) # GOOD WORKING CODE

terry.swim()

terry.swim_backwards()

print()
