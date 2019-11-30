# This script is about if-else statement
# related to US citizens who are eligible to Vote

fname = input('Enter your first name: ')

lname = input('Enter your last name: ')

age = int(input('Please enter your age: '))


if age >= 18:
   print(f'{fname.title()} {lname.title()}, You are eligible to vote!')
else:
   print(f'Sorry {fname.title()} {lname.title()}, wait until you turn 18 years old!')
