# This script not only prints a list but also added names to the list


word = ''

list = [ ]

while word != 'q':

    word = input('Enter a name: ').lower()

    if word != 'q':

        list.append(word)
    if word == 'ada' or word == 'sinach':
        print('A Nigerian Gospel Artist')
    elif word == 'lochard' or word == 'rene':
        print('An Haitian Gospel Artist')
    else:
        print('Keep guessing...!')
print('------------------------------------------------------')

for name in list:

    print(f"You entered {name.title()}")

print('You have exited the loop!')
