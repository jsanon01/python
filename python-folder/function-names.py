# This script prints a function with 3 different names

print('\nThis script prints a function with 3 dufferent names.')

print()

person = 'ada'

def greet(person):
    print(f'{person.title()} how are you?')
    print(f'what are you up to {person.title()}?')
    print(f"{person.title()} let's have some fun...")

greet(person)

print()

greet('emilie')

print()

greet('jacques saint-clair')

print()
