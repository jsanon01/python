"""


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

#sonson.customer_id()
#print(sonson)










#sophie = Person('sophia martelly'.title(), '305-451-9630', '38 Maple St, Queens, NY 10935')
#sophie.updateContact()

print()
