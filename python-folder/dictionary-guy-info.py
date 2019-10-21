# This script is about a person information using a dictionary
# Also it prints keys, values, and key-values respectively...

dictionary = {
		'first_name': 'pierre',
		'last_name' : 'bouquet',
		'current age'       : '44',
		'address'   : '110 jefferson dr',
		'city or town'      :'jeremie',
		'department'      : 'grand-anse',
		'country'   : 'haiti',
		}

#print(dictionary) # printing dictionary list
print('---------------------Printing Dictionary Keys----------------------')
for name in dictionary.keys(): # printing dictionary keys
    print(name.title())

print('---------------------Printing Dictionary Values----------------------')
for name in dictionary.values(): # printing dictionary values
    print(name.title())

print('---------------------Printing Dictionary Keys + Values----------------------')

for k, v in dictionary.items():
    print(f'{k.title()}:\t {v.title()}')
