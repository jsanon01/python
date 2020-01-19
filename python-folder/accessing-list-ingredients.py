
pizza = {
	'ingredients': ['cheese', 'onion', 'peperoni', 'sausage']
}


print('\nOriginal dictionary: keys and values only: ')
print(pizza)


print('\nAccessing: all values in the list: ')
print(pizza['ingredients'])


print('\nAccessing: 1st value in the list: ')
print(pizza['ingredients'][0])


print('\nAccessing: last value in the list: ')
print(pizza['ingredients'][3])

print('\nAccessing: keys and values together using for-loop: ')
for x in pizza.items():
    print(x)

print()
