"""
I want to initiate an empty dictionary
I want to initiate/label 4 keys and values inside that dictionary
I want to use for statement to print out dictionary's keys and values


"""


dictionary = {}

dictionary['american'] = ['tara combs']

dictionary['haitian'] = ['lochar remi']

dictionary['black'] = ['kirk franklin']

dictionary['african'] = ['sinach osinachi']


for k, v in dictionary.items():
    print('Performing Gospel artists: - {} --> {}'.format(k,v).title())

