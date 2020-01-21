"""
I want to print a dictionary with given keys and values
I want to delete key-value pairs using try-except function

"""

print("\nThis script prints out 'remaining' key-value pairs in a dictionary.")
print("\nOriginal list:\n{'year': 2018, 'Year': 2019 , 'years': 2020 }")

dictionary = {
		'year': 2018 ,
		'Year': 2019 ,
		'years': 2020 
		}

try:
    del dictionary['year']
    print('\nUpdated List:\n{}'.format(dictionary))

except:
    print('Key does not exist.')

print()
