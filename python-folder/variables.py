# This script prints separately several variables
# multiple variables are x, y, z (strings)

x, y, z = 'orange', 'bananas', 'pineapple'
print(x, y, z)
print()

# output variable
x = 'cool'
y = 'awesome'
print(f"Python is {x} and {y}!")
print()

# global variables 
a = 'indentation' # usually outside functions

def mufunction():
    print(f'Python loves {a}')

mufunction()
print()

# local variables 
a = 'indentation' 

def myfunction():
    b = 'fantastic' # usually inside functions
    print(f'Python loves {b}')

myfunction()
print()

# using global keyword
c = 'mango'

def fruits():
    global c
    c = 'apple' # to change global variable
    print(f'I love {c} very much')

fruits()
print()

# checking if item exists in a list
veggies = ['avocados', 'potatoes', 'peanuts', 'carrots']

for salad in veggies:
    print(f'List of veggies are: {salad.title()}')

