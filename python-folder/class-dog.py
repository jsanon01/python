# Class Dog

class Dog: # defining dog's class and properties
    def __init__(self, color, name, age, race):
        self.name = name
        self.age = age
        self.color = color
        self.race = race

# defining 3 functions aloowing 3 dog's activities
    def sit(self):
        print(f'{self.name} can sit down when asked')

    def roll_over(self):
        print(f'{self.name} will roll over')

    def bark(self):
        print(f'{self.name} barks loudly!')

# making 2 instances from dog's class
my_dog = Dog('golden', 'Willie', 6, 'German shepherd')

# printing dog's class and properties
print(f'My dog name is  {my_dog.name}.')
print(f'{my_dog.name} race is {my_dog.race}.')
print(f'{my_dog.name} age is {my_dog.age} years old.')
print(f'{my_dog.name} color is {my_dog.color}!')

# calling the pre-assigned functions
my_dog.sit()
my_dog.roll_over()
my_dog.bark()
