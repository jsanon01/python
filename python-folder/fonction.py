# This script passes 2 arguments to a function

fname = input('Enter first name: ')

lname = input('Enter last name: ')

city = input('Enter city: ')

country = input('Enter country: ')

def greet_user(fname, lname):
    print(f'Hello {fname.title()} {lname.title()}!')

def origin(city, country):
    print(f"{fname.title()} {lname.title()} is from {city.title()},{country.title()}")


greet_user(fname, lname)

origin(city, country)
