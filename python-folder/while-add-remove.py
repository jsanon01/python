# This script is about a list using while-loop

pets = ['bird', 'goose', 'duck', 'ant', 'cat', 'dog']

print(pets)

print()


while 'cat'in pets:
    pets.remove('cat') # removing cat from list (NOT WORKING)
    pets.append('german shepherd') # adding german shepherd from list

print(pets)
