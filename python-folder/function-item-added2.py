cart = []

item = ''

print('This script not only adds items but also prints them.')
 
x = input("Functions: 'add/show/ 'q' for quit: ")

while True:
    item = input('Enter input: ')
    if item == 'q':
        break

    elif item == 'add':
        addItem(item)
    elif item == 'show':
        showCart()
    else:
        print('Want to add more?: ')


#def main():
    
    def addItem(item):
        cart.append(item)
        print('Items added: {}'.format(item))
    addItem(item)

    x = input('add/show/quit: ')

    def showCart():
        for item in cart:
            print('- {}'.format(item))
    showCart()

print('The following items have been added:\n - {}'.format(cart))

#main()
