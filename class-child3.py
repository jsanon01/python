"""
I want to define a class named Person
I want to define a constructor method with 2 class attributes:
- firstname and lastname
I want to define a class method named phone
I want to define a class method named show_full_name
I want to create instance variable name person1

"""
class Person:

    def __init__(self):
        self.firstname = input('\nEnter first name:  ').title()
        self.lastname = input('\nEnter last name:  ').upper() 

    def phone(self):
        self.phone = int(input('\nEnter phone number: '))

    def show_full_name(self):
        print('\nFirst name: {}\nLast name: {}\nPhone number: {}'.format(self.firstname, self.lastname, self.phone))
#         print(self.firstname + ' ' + self.lastname) # GOOD CODING

#creating an object with the class
person1 = Person()
person1.phone()
person1.show_full_name()
print()
