"""
I want to initiate an empty dictionary
I want to initiate/label 4 keys and values inside that dictionary
I want to use for statement to print out dictionary's keys and values

I want to print out the dictionary
I want to print out the dictionary using for-loop

"""


dictionary = {}

dictionary['american'] = ['tara combs']

dictionary['haitian'] = ['lochar remi']

dictionary['black'] = ['kirk franklin']

dictionary['african'] = ['sinach osinachi']

print('\n--------- This script prints out regular dictionary ----------')

print('{}'.format(dictionary).title())

print('\n--------- This script uses for-loop to print out same dictionary ----------')

for k, v in dictionary.items():
    print('Performing Gospel artists: - {} --> {}'.format(k,v).title())

print()
