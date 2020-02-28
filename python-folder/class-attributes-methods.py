"""
I want to define 2 classes Cat and Dog respectively
I want to create 2 class methods inside of them
I want to print them out

"""
print('\nThis script is from class Cat(): ')

class Cat:
    age = 10
    def anniversaire(self):
        self.age -= 1

kitty = Cat()

kitty.anniversaire()

print('Kitty is {} year-old.'.format(kitty.age).title())

print('\nThis script is from class Dog(): ')

class Dog:
    age = 10
    def happyBirthday(self):
        self.age += 1

sam = Dog()

sam.happyBirthday()

print('Sam age is {} year-old.'.format(sam.age).title())

print()

