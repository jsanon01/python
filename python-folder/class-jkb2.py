"""
I want to define a class named JKB()
I want to define 4 class methods inside JKB
I want to print out these class methods

"""
print('\nThis script prints out 4 class methods and attributes')

class JKB:

    def moron(self):
        print("\nLe Departement de la Grand-Anse est divise en 3 arrondissements:\n'Jeremie', 'Anse Dainault', 'Corail'")

    def leon(self):
        print("L'arrondissement de Jeremie a 6 communes:\n'Jeremie','Abricots','Bonbon','Chambellan','Mafranc','Moron''")

    def marfranc(self):
        print("L'arrondissement de Anse-Dainault a 3 communes:\n'Anse-Dainault','Dame-Marie','Les Irois''")

    def bonbon(self):
        print("L'arrondissement de Corail a  4 communes:\n'Corail','Beaumont','Pestel','Roseaux'")



darline = JKB()

darline.moron()

print()

amelie = JKB()

amelie.leon()

print()

yvette = JKB()

yvette.marfranc()

print()

yvon = JKB()

yvon.bonbon()

print()
