"""
I want to define a class named Shark
I want to initialize name and age using __init__
I want to define a class method named swim
I want to define a class method named awesome

I want to define a main loop with the following:
- creating an instance in class  Shark
- calling swim method
- calling awesome method
"""

class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swim(self):
        print(self.name + ' is swimming'.title())

    def awesome(self):
        print(self.name + ' is pretty.'.title())

def main():
    sammy = Shark('ginadelle'.upper(), 7)
    print()
    sammy.swim()
    print()
    sammy.awesome()

#if __name__ == '__main__':

main()

print()
