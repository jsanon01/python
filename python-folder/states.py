# This script prints 3 states by numbers


def states(county):

    switcher = {
	
	1: 'florida',
	2: 'alabama',
	3: 'georgia'

	}
    return switcher.get(county, 'Invalid Entry')


print('This script prints 3 states by numbers 1-3: ')

state = ''

while state != 'q':

    if state.isdigit():

        result = states(int(state))

        print('You entered {}'.format(result).title())

    state = input('Enter state: ')

