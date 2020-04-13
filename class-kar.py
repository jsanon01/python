
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
