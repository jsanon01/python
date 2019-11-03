# This script prints contents of a list 
#!/bin/env python3

mountains = ['castaches','abricots', 'leon', 'bois-sec', 'bouda-mouille', 'duchiti']

mountains.sort()

print('Here are the following mountains in Grand-Anse Department:')

for mountain in mountains:
    print(mountain.title())
