"""
I want to define a class named Shark
I want to call the class Shark
------------------------------------
I want to define a class named Dauphin
I want to define a constructor method __init__
I want to define a method called swim()
I want to define a method called bouncing()
I want to create an instance or an object from the class

"""

class Shark:
    def __init__(self):
            print('\nconstructor method is used to initialize data...'.upper())
            print("\nthe 1st definition of a class, it always looks like this:\nwhen using the init method... '__init__(self):\n ")
    
Shark()

print('----------------Another Example----------------------\n')

class Dauphin:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def swim(self):
        print(self.fname + ' is swimming'.title())
    
    def bouncing(self):
        print(self.lname +  ' is bouncing in the water.'.title())

# kiki is an object from class Dauphin
kiki = Dauphin("leroi".title(), 'polo'.title()) # here we initialized the object 'kiki' by setting it equal to Dauphin()

# here are 2 methods from the class Dauphin
kiki.swim()

kiki.bouncing()

print()
