# This script is about a dictionary storing people's favorite numbers

dictionary = {
		'pierrot':'53',
		'jacques': '98',
		'elienne': '32',
		'michel': '78',
		'josue': '65',
		'merilien': '22'
		}

#for name in dictionary:
#    print(name)
print('----------------------Printing Dict Keys-Values---------------------------')
for key, value in dictionary.items():
    print(f"{key.title()}'s favorite number is {value.title()}")

print('----------------------Printing 1 Value based on 1 Key--------------------')
number = dictionary['pierrot'].title()

print(f"Pierrot's favorite number is {number}.") 
