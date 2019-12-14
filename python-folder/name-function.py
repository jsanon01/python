# this script prints out  a function 

print()

print('This script prints out a function,\nThus Local has priority over Global variable') 

name = 'dimitri vorbe' # global variable

def myName(name):

    name = 'reginald vorbe' # local variable

    print(f'My name is:  {name.title()}')

myName(name)

print()
