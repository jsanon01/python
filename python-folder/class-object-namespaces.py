"""
I want to define a class named Person
I want to define a class attribute named species
I want to print the value of class attribute

I want to define a class named Person
I want to define a class named Person

"""
class Person:
    species = 'equal'

# printing the value inherited from the class attribute
print('all men are created {}...'.format(Person.species).upper())

# accessing the class
Person.alive = True
print('we only live once: {}'.format(Person.alive))

# instantiating
man = Person()
print('are all men created {}?'.format(Person.species))

man.firstname = 'ti paul'
man.lastname = 'valcourt'
print('first name: {}\tlast name: {}'.format(man.firstname, man.lastname))
