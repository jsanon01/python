# This script clears items from cart

cart = ['bananas','carrots','milk','jiuce','apples']

print('\nHere is the list of items in cart: ')


for item in cart:
    print('- {}'.format(item).title())

print('\n------- This script prints items and clears the shopping cart -----')

def clearItem():
    cart.clear()
    print('\nYour cart is empty NOW.'.format(item))


clearItem()

print()

