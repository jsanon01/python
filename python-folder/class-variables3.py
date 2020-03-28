"""
I want to define a class named Shark
I want to define a constructor method with 2 class variables: name and age
I want to define another class variable named followers

I want to define a function name main()
I want to define an instance variable named sammy
I want to print out the instance variable named sammy
https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3
"""

# defining a class 
class Shark:

    # defining a constructor with 2 instance variables: name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # defining a method with instance variable followers
    def set_followers(self, followers):
        self.followers = followers

def main():

    # 1st object, instance variable of constructor method
    sammy = Shark('sammy',6)
    jeremie = Shark('piskettes', 24)

    # printing out intance variable
    print('\n{} is {} year-old.'.format(sammy.name.upper(), sammy.age))
    print('\n{} come out around August {}th of each year.'.format(jeremie.name.upper(), jeremie.age))

main()

print()
