"""
I want to define a class named Dog
I want to define a class method accepting parameters
I want to define a class named Dog
I want to define a class named Dog
"""
print('\nThis script prints out 2 arguments that was passing to 2 class methods.\n')

class Dog:
    def showAge(self, age):
        print('Ada age is: {} years old...'.format(age))

    def showNationality(self, nationality):
        print('Okinawa nationality is: {}...'.format(nationality).title())

ada = Dog()

ada.showAge(22)

print()

okinawa = Dog()

okinawa.showNationality('nigerian')

print()
