# Inheritance Script

class Jeremie():
    def __init__(self, fname,lname):
       self.firstname = fname
       self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

print('--- Les Notables de la Grand-Anse ---')
a = Jeremie('Brunel Pierre -->', 'Jeremie')
a.printname()

x = Jeremie('Antoine Verrier -->', 'Jeremie')
x.printname()

y = Jeremie('Hismero -->', 'Beaumont')
y.printname()

z= Jeremie('Fignole -->', 'Abricots')
z.printname()


print('--- Notables Jeremiens @ Port-au-Prince ---')
class Arrondissement(Jeremie):
    pass

b = Arrondissement('Lesly Brezault -->', 'Lesly Center | Gambling')
b.printname()

c = Arrondissement('Patrick Monsignac -->', 'Radio Caraibes | Media')
c.printname()

d = Arrondissement('Eddy Rene -->', 'Dieu Qui Decide | Transportation')
d.printname()
