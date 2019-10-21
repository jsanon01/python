# This script gets keys from a dictionary

dictionary = {
     	"Brand" : "Kia",
	"Model" : "Sorrento",
	"Year" : "2014"
		}

dictionary["Brand"] = 'Chevy'

dictionary["Model"] = 'Traverse'

dictionary["Year"] = '2020'


kiki = dictionary.get('Brand') # accessing value

kika = dictionary.get('Model') # accessing value

kiko = dictionary.get('Year') # accessing value

print('--------------------Printing Updated Dictionary ---------------------')
print(dictionary) 

print('--------------------Printing Dictionary Values---------------------')

print(f'Brand is {kiki}')

print(f'Model is {kika}')

print(f'Year is {kiko}')

print('--------------------Printing Dict Keys + Values---------------------')

for k, v in dictionary.items():
      print(f'{k}:\t {v}')
