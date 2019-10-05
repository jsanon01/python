# Inheritance Script 

class Gerard():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Gerard('Rousseline', 'Gerard')
x.printname()

y = Gerard('Primose', 'Gerard')
y.printname()

z = Gerard('Patrick','Gerard')
z.printname()

class Etienne(Gerard):
    pass

a = Etienne('Yvon', 'Jean')
a.printname()
