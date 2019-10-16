# This script is about Inheritance
# Defining a class which inherited from another class


class Person: # creating Parent class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
print('------------------Ex-Presidents Class-----------------------')
x = Person("Jean-Claude", "Duvalier")
x.printname()

y = Person("Rene", "Preval")
y.printname()

# creating Student class
print('------------------Student Class-----------------------')
class Student(Person):
    pass

z = Person('Joel', 'Pierre-Fils')
z.printname()

zi = Person('Amos', 'Antoine')
zi.printname()
print('------------------Hollywood Class-----------------------')

class Hollywood(Person):
    pass

a = Person('Joe','Pecci')
a.printname()

b = Person('Bob','Derose')
b.printname()

