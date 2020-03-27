"""
I want to define a function with 2 values
I want to define a variable with a dictionary as values
I want to instantiate an object named musician
I want to print the object name musician

"""

def build_person(first_name, last_name, age):
    person = {'First': first_name, 'Last': last_name, 'Age': age}
    return person

musician = build_person('eric'.title(), 'laguerre'.upper(), 61)

print()

print(musician)

print()
