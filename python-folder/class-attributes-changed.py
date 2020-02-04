"""
I want to create a class named 'Animals'
I want to create 2 instances from that class
I want to print them out

I want to access (modify) these instance attributes
"""

class Animals():
    male = 'lion is the king of animals..'
    female = 'tiger is from bobcat family...'


lion = Animals()

tiger = Animals()

lion.male = "Lion symbolyzes Juda's Tribe..."

tiger.female = 'Tiger is tame comapared to the others... '


print("\nThis script changes Instance Attributes.")

print('\n---------------------- Original Script ---------------------------')

print("Here are some Animal characteristics:\n'lion is the king of animals..\n'tiger is from bobcat family...'\n")

print('---------------------- New Script ---------------------------')

print('\nHere is few characteristic of Lion:\n{}'.format(lion.male).title())

print()

print('Here is few characteristic of Tiger:\n{}'.format(tiger.female).title())

print()
