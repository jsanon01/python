# This script prints keys-values of a dictionary

print('Please enter one of the following names:\nJim, Peter, Zoe and Abel')

person = input('Get age for: ').lower()

while person != 'q':

    ages = {'jim': 44, 'peter': 22, 'zoe': 11, 'abel': 50}

    print(f'{person.title()} is {ages[person]} years old!')

    person = input('Get age for: ').lower()
