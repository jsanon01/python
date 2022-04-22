# Script is about Inheritance
# Script prints out 1 class + 2 functions (names | print)
# calling class + printname

class Gauthier:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
       print(self.firstname, self.lastname)

ben = Gauthier('Ben', 'Gauthier')
ben.printname()

franckel = Gauthier('Franckel', 'Gauthier')
franckel.printname()

ducarte = Gauthier('Ducarte', 'Gauthier')
ducarte.printname()

class Cousin(Gauthier):
    pass

print('---Cousins and Siblings---')

a = Cousin('Famille', 'Auguste')
a.printname()

b = Cousin('Famille', 'Josma')
b.printname()

c  = Cousin('Famille', 'Joseph')
c.printname()
