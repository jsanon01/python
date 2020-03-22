"""
I want to define a class named Shark
I want to define a class variable named animal
I want to define a class named location
I want to define a class named followers

I want to print all the class variables in one line
"""


class Shark:
    animal = 'dolphins'
    location = 'ocean atlantic'
    followers = 5

new_shark = Shark() # instantiating new_shark

#print(new_shark.animal) # class varaible (GOOD CODING WILL PRINT SEPARATELY)

#print(new_shark.location) # class variable (GOOD CODING WILL PRINT SEPARATELY)

#print(new_shark.followers) # class variable (GOOD CODING WILL PRINT SEPAARATELY)

print('\n{} often go to the {} with {} followers.\n'.format(new_shark.animal, new_shark.location, new_shark.followers).title())
