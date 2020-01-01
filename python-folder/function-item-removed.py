# This script prints out removed items

print('\nThis script prints out Removed Items')


cart = ['carrots','lettuce','broccoli','mangos','rice','milk' ] 

item = ''

print('\nHere are the following items in the list: ')

for item in cart:
    print(' - {}'.format(item))

print()

# This line below works fine
# print("\nOriginal list: ['leon','marfranc','bouda','mouille','bois-sec','jeremie' ]")

while True:

    item = input('Enter input: ')

    if item == 'q':
        break

    def removeItem(item):

        try:
            cart.remove(item)
            print('{} has been removed.'.format(item))

        except:
            print("Sorry, this item cannot be removed or does not exist.")


    removeItem(item)


print('The following item(s) remain in the list:\n {}'.format(cart))
