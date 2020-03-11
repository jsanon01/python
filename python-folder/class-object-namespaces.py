"""
I want to define a class named Person
I want to define a class attribute named species
I want to print the value of class attribute

I want to instantiate 
I want to define a class named Person

"""
class Person:
    species = 'equal'

# printing the value inherited from the class attribute
print('\nall men are created {}...'.format(Person.species).upper())

# accessing the class
Person.alive = True

print('\nwe only live once: {}'.format(Person.alive).title())

# instantiating
man = Person()

print('\nare all men created {}?'.format(Person.species).upper())

man.firstname = 'pierre-paul'

man.lastname = 'valcourt'

print('\nfirst name: {}\tlast name: {}'.format(man.firstname, man.lastname).title())

print()
