# This script changes a List item values by index

sports = ['basketball', 'football', 'tennis', 'LACROSSE']

def change(list):

    sports [ 3 ] = 'SOCCER' # either sports or list, no difference
#    list [ 3 ] = 'SOCCER' # either list or sports, no difference

print()

print('This script changes a List item values by index')

print('\nBefore the list has changed: {}'.format(sports))

change(sports)

print()

print('After the list has changed: {}'.format(sports))

print()
