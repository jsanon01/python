"""
I want to create a class named 'Animals'
I want to create 2 instances from that class
I want to print them out

"""
class Animals():
    male = 'lion is the king of animals..'
    female = 'tiger is from bobcat family...'

lion = Animals()

tiger = Animals()

lion.male = 'clarice and actimed'

tiger.female = ' '


print('\nThis script changes Instance Attributes.\nOriginal script: ')

print('\nHere is few characteristic of Lion:\n{}'.format(lion.male).title())
print()
print('Here is few characteristic of Tiger:\n{}'.format(tiger.female).title())
print()
