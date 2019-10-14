# This script is about parenthood
# M for son if age is lower than 18 (else daughter)
# M for father if age is between 18 and 65 (else father)
# M for grandfather if age is over 65 (else grandmother)


fname = input('Enter first name: ')

lname = input('Enter last name: ')

age = int(input('Enter age: '))

gender = input('Enter gender: ')

if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')
print(f'{fname.title()} {lname.title()} is {age} years old...!')
