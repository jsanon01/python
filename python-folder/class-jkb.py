"""
I want to define a class named JKB()
I want to define 2 class methods inside JKB
I want to print out these class methods

"""
print('\nThis script prints out 2 class methods and attributes')

class JKB:
    def moron(self):
        print("\nLes habitants de Moron s'appellent: 'Moronais'")
    def leon(self):
        print("Les habitants de Leon s'appellent: 'Leonnais'")
    def marfranc(self):
        print("Les habitants de Leon s'appellent: 'Marfrancois'")


darline = JKB()

darline.moron()

print()

amelie = JKB()

amelie.leon()

print()

yvette = JKB()

yvette.marfranc()

print()
