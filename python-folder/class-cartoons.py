"""
I want to define a class named Cartoons
I want to define a class methods inside class Cartoons
I want to call these class methods

"""

class Cartoons:
    def pbs(self): 
        print(f"'Daniel the tiger', 'Superwhy','nature cat'".title())

    def qubo(self):
        print(f'the cat with the hat knows a lot about that'.title())

    def daystar(self):
        print(f'DayStar is an evanlegical tv channel broadcasting worlwide'.title())


print("\nThis script prints out class methods with 'self' parameters: ")
daniel = Cartoons()
print()
daniel.pbs()

nadia = Cartoons()
print()
nadia.qubo()
print()

tv = Cartoons()
print()
tv.daystar()
print()

