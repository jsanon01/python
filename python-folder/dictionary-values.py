# This script is about PRINTING NEW  values from a dictionary
# Using get() to access values

dictionary = {
     	"Brand" : "Kia",
	"Model" : "Sorrento",
	"Year" : "2014"
		}

dictionary["Brand"] = 'Range Rover'

dictionary["Model"] = 'HSE'

dictionary["Year"] = 2020

kiki = dictionary.get('Brand') # accessing value

kika = dictionary.get('Model') # accessing value

kiko = dictionary.get('Year') # accessing value

print("Printing dictionary's list: ") 
print(dictionary) 

print("Printing dictionary's NEW values: ") 

print(kiki)

print(kika)

print(kiko)


