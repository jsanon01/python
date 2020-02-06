"""
I want to define a class Cars
I want to define different values for multiple instances

"""
print('\nThis script prints...')

class Cars():
    def __init__(self, year, brand, color):
        self.year = year # setting attribute year to the value passed
        self.brand = brand # setting attribute brand to the value passed
        self.color = color # setting attribute color to the value passed

bmw = Cars(2020, 'bmw', 'red') # creating 2020 BMW red car object

nissan = Cars(2017, 'Nissan', 'blue') # creating 2017 Nissan blue car object

audi = Cars(2019, 'AUDI', 'white') # creating 2019 AUDI white car object

#Cars.sort()

print(bmw.year, bmw.brand.upper(),bmw.color.title())

print(audi.year, audi.brand, audi.color)

print(nissan.year, nissan.brand, nissan.color)

print()
