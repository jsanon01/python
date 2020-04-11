# This script is about Dog Class


class Dog: # defining dog class
    # defining dog properties
    def __init__(self, color, name, age, race):
        self.name = name
        self.age = age
        self.color = color
        self.race = race

# defining dog activities
    def sit(self):
        print(f'\n{self.name} is  now sitting down')

    def roll_over(self):
        print(f'\n{self.name} will roll over')

    def bark(self):
        print(f'\n{self.name} barks loudly!')

# making an instance
my_dog = Dog('golden', 'Willie', 6, 'German shepherd')

# printing dog attributes
print(f'\nMy dog name is  {my_dog.name}.')
print(f'\n{my_dog.name} race is {my_dog.race}.')
print(f'\n{my_dog.name} age is {my_dog.age} years old.')
print(f'\n{my_dog.name} color is {my_dog.color}!')

print('\n ------- Dog activities ---------')
# calling functions for dog activities
my_dog.sit()
my_dog.roll_over()
my_dog.bark()
print()
