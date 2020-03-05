"""

the magic method is: __str__

"""

class Cat:
    def __str__(self):
        return 'this is a kitty'.title()

sam = Cat()

print(sam)

print('--------------------------')

class Lion:
    def __str__(self):
        return "the lion of juda's tribe"

kiki = Lion()

print(kiki)

