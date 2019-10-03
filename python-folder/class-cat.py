# Class Cat

class Cat: # defining cat's class and properties
    def __init__(self, name, age, race, owner):
        self.name = name
        self.age = age
        self.race = race
        self.owner = owner

# defining 3 functions aloowing 3 cat's activities
    def sit(self):
        print(f'{my_cat.name} sits down when happy.')

    def meow(self):
        print(f'{my_cat.name} always meows when hungry.')

    def hide(self):
        print(f'{my_cat.name} hides in basement when sleepy.')

# instantiation
my_cat = Cat('Todda', 7,'Persian', 'Sandy') # making instance from class

your_cat = Cat('April',9,'Bata', 'Lauper') # making instance from class

# printing cat's class and properties
print('--- Here are some characteristics of the Cat ---')
print(f'My cat name is {my_cat.name}')
print(f'{my_cat.name} age is {my_cat.age} years old.')
print(f'{my_cat.name} race is {my_cat.race}')
print(f'{my_cat.name} owner is {my_cat.owner}')
print('---------------------------')
print(f'Your cat name is {your_cat.name}')
print(f'{your_cat.name} is {your_cat.age} years old.')
print(f'{your_cat.name} race is {your_cat.race}')
print(f'Jenna {your_cat.owner} is the owner of {your_cat.name}')

print('--- Here are some actions of the Cat ---')
my_cat.sit()  # calling method
my_cat.meow() # calling method
my_cat.hide() # calling method
print('------------------------')
your_cat.sit()
your_cat.hide()
your_cat.meow()
