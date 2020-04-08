"""
I want to define a class named Person
I want to define a custom constructor method with the following values:
- name, phone, address
I want to define a function named updateContact
I want to instantiate the object named ana (aka instance variable)
I want to define a sub-class named Customer
I want to define instance variable named sonson

"""


class Person:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def updateContact(self):
        print("\nName: {}\tPhone: {}\tAddress: {}".format(self.name, self.phone, self.address))

ana = Person('ana pierre'.title(), '781-781-6987', '12 Main St, Norwood, MA 02062')
ana.updateContact()

class Customer(Person):
    def customer_id(self):
        print('employee id: {}'.format(self.customer_id))

sonson = Customer('patrick joseph'.title(), '202-147-9875', '196 eugene margron, jeremie'.title())
sonson.updateContact()

joel = Customer('joel auguste'.title(), '305-949-7446', '510 NE 163 St, Miami, FL 33042')

joel.updateContact()

sophie = Person('sophia martelly'.title(), '305-451-9630', '38 Maple St, Queens, NY 10935')
sophie.updateContact()

print()
