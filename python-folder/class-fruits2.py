"""
I want to define a class named Fruits()
I want to define some attributes inside the class named Fruits()
I want to print out these attributes related to class named Fruits()
"""

class Fruits():
    def __init__(self, apples, bananas, mangos):
        self.apples = apples # setting attribute to the value passed
        self.bananas = bananas # setting attribute to the value passed
        self.mangos = mangos # setting attribute to the value passed

zabokas = Fruits('imported', 'local produce', 'local produce')

apples = 'few people eat apples'
bananas = 'popular and year-around'
mangos = 'popular and seasonable'

print('\nHere are some favorite Haitian fruits:\n- Apples are {}\n- Bananas are {}\n- Mangos are {}'.format(zabokas.apples, zabokas.bananas, zabokas.mangos))

print()
print('-------------------------------------------------------')
print('\nHere are some of their characteristics:\n ')

pomme = Fruits('rich in glucose','seasonal', 'alcohol-compatible')

figues = Fruits('rich in potasium', 'year-around', 'popular')

mangues = Fruits('rich in glucose', 'seasonable', 'summer-relief')

print(pomme.apples, pomme.bananas, pomme.mangos)

print(figues.apples, figues.bananas, figues.mangos)

print(mangues.apples, mangues.bananas, mangues.mangos)
