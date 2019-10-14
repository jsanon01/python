# This script is about Nested if-else statement
# related to Voting Age

fname = input('Enter first name: ')

lname = input('Enter last name: ')

age = int(input('Enter age: '))

gender = input('Enter gender: ')

if age < 18:
    if gender == 'M':
        print('Not eligible to vote...')
    else:
        print('Not eligible to vote...')
elif age >= 18 and age < 95:
    if gender == 'M':
        print('Eligible to vote...')
    else:
        print('Eligible to vote...')
else:
    if gender == 'M':
        print('Eligible to vote...')
    else:
        print('Eligible to vote...')
        print(f'{fname.title()} {lname.title()} is {age} years old...!')
