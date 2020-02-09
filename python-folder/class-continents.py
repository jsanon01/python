"""
I want to define a class named Continents()
I want to define some attributes inside the class named Continents()
I want to print out these attributes related class named Continents()

"""

class Continents():
    def __init__(self, africa, america, asia, europe, oceany):
        self.africa = africa
        self.america = america
        self.asia = asia
        self.europe = europe
        self.oceany = oceany

ethiopa = Continents('is in the bible', 'is the new world', 'is in Mesopotania', 'is home of Ancient Greeks', 'is home of borneo')

print(ethiopa.africa, ethiopa.america, ethiopa.asia, ethiopa.europe, ethiopa.oceany)
