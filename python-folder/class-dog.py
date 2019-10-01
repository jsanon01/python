# Class Dog

class Dog:
    def __init__(self, color, name, age, race):
        self.name = name
        self.age = age
        self.color = color
        self.race = race

    def sit(self):
        print(f'{self.name} is  now sitting down')

    def roll_over(self):
        print(f'{self.name} will roll over')

    def bark(self):
        print(f'{self.name} barks loudly!')

my_dog = Dog('golden', 'Willie', 6, 'German shepherd')

print(f'My dog name is  {my_dog.name}.')
print(f'My dog race is {my_dog.race}.')
print(f'My dog age is {my_dog.age} years old.')
print(f'My dog color is {my_dog.color}!')

my_dog.sit()
my_dog.roll_over()
my_dog.bark()
