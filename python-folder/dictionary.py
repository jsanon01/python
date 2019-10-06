# Script is about a dictionary

# setting up dictionary with keys and values
dictionary = {
     	"brand" : "Kia",
	"model" : "Sorrento",
	"Year" : "2014",
       # "size" : "Sedan"
		}
# accessing dictionary's value
kiki = dictionary.get('model') 

# updating dictionary's values
dictionary["Brand"] = "Chevy"
dictionary["Model"] = "Traverse"
dictionary["Year"] = 2019
dictionary["Size"] = "SUV"

# printing dictionary keys and values
print(dictionary) 
