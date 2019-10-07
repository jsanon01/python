# This script makes a loop through key-value pairs

user_0 = {
                'first': 'pierre',
                'last': 'sanon',
                'username':'psanon',
		'email' : 'psanon@gmail.com'
        }

for key in user_0.keys():
    print(f' Key is {key.title()}')

print()

for value in user_0.values():
    print(f' Value is {value.title()}')
