# This script prints key, values, and key-value pairs separately...

print('--- Printing keys in dictionary ---')

rivers = {
	'nile' : 'egypt',
	'voldrogue' : 'haiti',
	'baharona' : 'dominican republic',
	'ti-guinaudee' : 'la martinique'
	}

for river in rivers.keys():
    print(f"{river.title()} goes to the sea!")

print('--- Printing values in dictionary ---')

for river in rivers.values():
    print(f'{river.upper()} is a country!')

print('--- Printing keys and values in dictionary ---')

for k, v in rivers.items():
    print(f'{k.title()} runs throuh {v.title()}!')
