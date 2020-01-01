# This script prints Added item in a function

cart = [ ]

item = ''

print('\nThis script prints Added item in a function.')

while True: 

    item = input('Enter input: ')

    if item == 'q':
        break

#    elif item.isdigit() and item  > 2:
#        print('do you want to add more item?: ')

#    else:
#        print('Added Items: {}'.format(cart))


    def addItem(item):

        cart.append(item)

        print('{} has been added.'.format(item).title())

    addItem(item)


#print('The following items have been added:\n {}'.format(cart))

print(f'The following items have been added:\n {cart}')

print()

