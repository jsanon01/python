# This script prints contents of a list 
#!/bin/env python3

print()

mountains = ['castaches','abricots', 'leon', 'bois-sec', 'bouda-mouille', 'duchiti']

mountains.sort()

print('This script prints out the following mountains in Grand-Anse Department: ')

for mountain in mountains:
    print(f'Here are the following mountains in Grand-Anse Department: {mountain.title()}')

print()
