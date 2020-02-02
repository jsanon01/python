"""
I want to define a class named Vehicle
I want to print out the memory location of that class

I want to define a class named Car
I want to create 2 objects from the class Car
I want to print them out

"""

class Vehicle():
    pass

kia = Vehicle()

print('\nMemory location of the class Vehicle():\n {}'.format(kia))
print()

print('--------------------------------------------------------------------')

class Car():
    pass

bmw = Car() # creating instance & storing it in bmw's variable

ford = Car()

print("\nNumerical representation of memory location of variable bmw':\n'bmw = Car' ")
print(hash(bmw))

print("\nNumerical representation of memory location of variable ford':\n'ford = Car' ")
print(hash(ford))
print()
