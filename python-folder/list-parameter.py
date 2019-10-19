# This script passes a List as Parameter
print('Script passes a List as Parameter')

def my_function():
    for x in fruits:
        print(x.title())

fruits = ['bananas', 'oranges', 'avocados', 'quenepes']

my_function()

print('-------------------------')

# This script passes a List as Parameter (demo from W3School.com)
print('Script passes a List as Parameter')

def function(food):
    for x in food:
        print(x.upper())

veggies = ['carrots', 'beans', 'sweet potatoes', 'brocoli']

function(veggies)

print('-----------------------')
# This script passes a List as Parameter (demo from W3School.com)
print('Script calculates return values from calling function')

def fonction(x):
    return 5 * x

#print('fonction' * ( 3) # script will be displayed 3 times
print(fonction(4)) # return value x calling fonction
print(fonction(10)) # return value x calling fonction
