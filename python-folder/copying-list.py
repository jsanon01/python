# This script not only prints a list but also a list-copy

print()

print('This script prints 2 original lists: ')

data = [10, 20, 30, 40, 50]

data2 = ['jean', 'paul', 'belmondo']

print(' {}\t\t {}'.format(data, data2).title())

print('-------------------------------------------------')

print('This script prints 2 copies of the 2 original lists: ')

data_copy = data[:]

data_copy2 = data2[ : ]

print('{}\t\t {}'.format(data_copy, data_copy2).title())

print()
