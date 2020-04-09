"""
I want to define a class named Person
I want to define a constructor method with self
I want to define a method named info
I want to create an instance variiable named ana

"""

class Person:
    def __init__(self):
        self.fname = input('Enter first name: ').title()
        self.lname = input('Enter last name: ').title()
        self.phone = input('Enter phone number: ')
        self.address = input('Enter address: ').title()

    def info(self):
        print('\nFirst name: {}\nLast name: {}\nPhone: {}\nAddress: {}'.format(self.fname, self.lname, self.phone, self.address))

ana = Person()
ana.info()
print()








"""
def main():
#    ana = Person(' ',' ')
    fname = input('enter first name: ')
    lname = input('enter last name: ')
#    ana = Person(' ',' ')

main()
"""
