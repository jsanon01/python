"""
I want to create a class Bird
I want to create 3 functions inside the class Bird:
- intro  - flight  - eat
I want to create a child class named sparrow
I want to create a child class named ostrich
I want to make 3 object instances and call them:
- kiki  - kika - kiko

"""

print('\n--------- polymorphism with inheritance -------------------'.title())

class Bird:
    def intro(self):
        print('\nthere are many types of birds.'.title())

    def flight(self):
        print('\nbirds can survive during their flight.'.title())

    def eat(self):
        print('\nall birds eat nuts.'.title())


class sparrow(Bird):
    def flight(self):
        print('\nsparrow fly from north to south.'.upper())

class Ostrich(Bird):
    def flight(self):
        print('\nostrich fly form east to west.'.upper())

kiki = Bird()
kika = sparrow()
kiko = Ostrich()


kiki.intro()
kiki.flight()
kiki.eat()

print('\n-------------------------------------------')

kika.intro()
kika.flight()
kika.eat()
print('\n-------------------------------------------')

kiko.intro()
kiko.flight()
kiko.eat()

print()
