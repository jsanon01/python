"""
I want to define a class named Shark
I want to define 2 functions inside the class named Shark
- swim()
- awesome()

I want to create an object inside the class
I want to create a method inside the class

"""

class Shark: # defining class

    def swim(self): # defining function
        print('\nthe shark is swimming...'.title())

    def awesome(self): # defining function
        print('\nthe shark is awesome...'.title())


# object is an instance of a class
sammy = Shark() # Shark object is called sammy (or we can say we initialized the object)

sammy.swim() # method used with Shark object

sammy.awesome() # method used with Shark object

print()

"""
--------- good OPTIONAL coding ------------
def main():
    # object is an instance of a class
    sammy = Shark() # Shark object is called sammy (or we can say we initialized the object)
    sammy.swim() # method used with Shark object
    sammy.awesome() # method used with Shark object

main()

"""
