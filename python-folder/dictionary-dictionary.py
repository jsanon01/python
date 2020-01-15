"""
I want to print a main dictionary and sub-dictionary with keys and values
I want to print a dictionary inside main dictionary with keys and values
I want to print indexes in a dictionary

"""

data = {
	'teams': 'Red Sox, Bruins, Patriots',
	'wins': {'year': 2018, 'score': '36-12'}
}

print("\nI want to print 'main & sub dictionaries with keys and values'")

print('{}'.format(data))

print('\nI want to print a dictionary inside main dictionary with keys and values')

print("The sub-dictionary here is 'wins':\n {}".format(data['wins']))

print("\nI want to print indexes inside sub-dictionary 'wins'")

print('Year: {}'.format(data['wins']['year']))

print('Score: {}'.format(data['wins']['score']))

print()
