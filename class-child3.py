"""
I want to 

"""
class Person:

    def __init__(self):
        self.firstname = input('Enter first name:  ').title()
        self.lastname = input('Enter last name:  ').upper() 

    def phone(self):
        self.phone = int(input('enter phone number: '))

    def show_full_name(self):
        print('First name: {}\nLast name: {}\nPhone number: {}'.format(self.firstname, self.lastname, self.phone))
#         print(self.firstname + ' ' + self.lastname) # GOOD CODING

#creating an object with the class
person1 = Person()
person1.phone()
person1.show_full_name()

