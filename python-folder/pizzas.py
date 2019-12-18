# This script prints a function along with a for-loop

def make_pizza(size, *toppings):
    print(f'\nMaking a {size}-inch pizza with the following toppings: ')

make_pizza(18)
#make_pizza(18, 'pepperoni') # good code

toppings = ['cheese','onions','green pepper','mushrooms','olive']

for topping in toppings:
    print(f'- {topping.title()}') # only one row will print
#    print(f'- {topping}') # toppings will print as a matrix (rows and columns)

