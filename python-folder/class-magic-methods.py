"""
I want to define 2 classes named Cat and Lion repectively
I want to define the magic method  __str__ for both classes
I want to use 'return' statement in magic method for both classes

"""
print("\nThis script prints out 2 classes using the magic method: '__str__'")

class Cat:
    def __str__(self):
        return '\nthis is a kitty...'.title()

sam = Cat()

print(sam)

print('\n---------------------------------------------------')

class Lion:
    def __str__(self):
        return "\nthe lion of juda's tribe...".title()

kiki = Lion()

print(kiki)

print()

