"""
I want to define a class named Dog
I want to define 2 class methods inside class Dog
I want to call these class methods

"""
class Dog:
    def makingsound(self):
        print('the dog barks to communicate with humans.'.title())

    def makesound(self):
        print('the kitty meows to express something: attention or food.'.title())

print('\nThis script prints out 2 methods from a class named Dog.')

sam = Dog()
print()
sam.makingsound()

kitty = Dog()
print()
kitty.makesound()
print()
