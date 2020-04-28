"""


"""

print('\n--------- polymorphism with inheritance -------------------'.title())

class Bird:
    def intro(self):
        print('\nthere are many types of birds.')

    def flight(self):
        print('\nbirds can survive during their flight.')

    def eat(self):
        print('\nall birds eat nuts.')


class sparrow(Bird):
    def flight(self):
        print('\nsparrow fly from north to south.')

class Ostrich(Bird):
    def flight(self):
        print('\nostrich fly form east to west.')

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
