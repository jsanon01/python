# This script is about Car rental

class Car:
    def __init__(self, brand, year, make, model, door, color):
        self.brand = brand
        self.year = year
        self.make = make
        self.model = model
        self.door = door
        self.color = color
    
#    def printname():
 #       print(f"'self.brand' = 'Kia', 'self.year' = '2019'.'self.make' = 'Sorento', 'self.model' = 'GDI', 'self.door' = '4-door', 'self.color' = 'white'")

my_car = Car('Kia', '2014', 'Sorrento', 'GDI', '4-door', 'white')

print('--- Here are the characteristics of the car I have rented ---')
print(f'Car name is {my_car.brand}')
print(f'The year is {my_car.year}')
print(f'The model is {my_car.model}')
print(f'The make is {my_car.make}')
print(f'Car has {my_car.door}')
print(f'And car color is {my_car.color}')
