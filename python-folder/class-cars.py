"""
I want to define a class Cars
I want to define different values for multiple instances

"""
print('\nThis script prints out attributes from class Cars()...')

class Cars():
    def __init__(self, year, brand, color):
        self.year = year # setting attribute year to the value passed
        self.brand = brand # setting attribute brand to the value passed
        self.color = color # setting attribute color to the value passed

bmw = Cars(2020, 'bmw', 'red') # creating 2020 BMW red car object

nissan = Cars(2017, 'nissan', 'blue') # creating 2017 Nissan blue car object

audi = Cars(2019, 'audi', 'white') # creating 2019 AUDI white car object

print()

print(bmw.year, bmw.brand.upper(),bmw.color.title())

print()

print(audi.year, audi.brand.upper(), audi.color.title())

print()

print(nissan.year, nissan.brand.upper(), nissan.color.title())

print()
