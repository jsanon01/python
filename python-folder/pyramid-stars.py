"""
I want to print a pyramid of stars by
- declaring variable
- using conditional statement (for loop)
- decrementing the variable


"""

print()

j = 9 # variable used for printing spaces

for i in range(1, 10,2):
    print(' '*j + i*'*')
    j = j -1

print('\n------------------------------------------')


j = 20

for z in range(1, 21,2):
    print(' ' * j + z * '*')
    j = j-1

print()

print('\n------------------------------------------')

j = 30

for i in range(1,31,2):
    print(' '*j+i*'*')
    j = j-1

print()
