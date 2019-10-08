# This script makes a loop through key-value pairs

user_0 = {
		'first': 'pierre',
		'last': 'sanon',
		'username':'psanon'
	}

for key, value in user_0.items():
    print(f'\nKey: {key.upper()}')
    print(f'\nValue: {value.upper()}')

