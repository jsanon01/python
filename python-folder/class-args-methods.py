"""
I want to define a class named Dog
I want to define a class method accepting parameters
I want to define a class named Dog
I want to define a class named Dog
"""
print('\nThis script prints out argument that was passing to class method')

class Dog:
    def showAge(self, age):
        print('Ada age is: {} years old'.format(age))

ada = Dog()

ada.showAge(22)

print()

#okinawa = Dog()

#okinawa.showAge(44)
