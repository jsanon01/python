# This script not only prints a list but also added names to the list


word = ''

list = [ ]

while word != 'q':

    word = input('Enter a name: ').lower()

    list.append(word)

for name in list:

#    print('You entered {}'.format(name).title())
    print(f"You entered {name.title()}")

print('You have exited the loop!')
