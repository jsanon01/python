"""
I want to define a class named Car
I want to construct __init__ method
I want to initialize 3 properties or attributes
- name, model, and year
I want to print out descriptive info about the car
I want to create a method named mileage
I want to create instance variables

"""
# a simple attempt to represent a car
class Car:

    # initializing attributes to describe a car
    def __init__(self):
        self.make = input('\nEnter make: ')
        self.model = input('\nEnter model: ')
        self.year = input('\nEnter year: ')



    # returning a neatly formatted descriptive information
    def info(self):
        print('\nYou have entered: {} {} {}'.format(self.make, self.model, self.year).title())

    # creating method
    def mileage(self):
        self.mileage = input('\nEnter the mileage: ')
        print("\nThis car has {} miles on it.".format(self.mileage))



# creating instance variables
my_car = Car()
my_car.info()
my_car.mileage()
print()
