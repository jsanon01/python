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

daniel = Cartoons()
print()
daniel.pbs()

nadia = Cartoons()
print()
nadia.qubo()
print()

