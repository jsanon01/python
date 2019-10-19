# This script is about while and if-else statement
# About who are eligible to vote



name = ''
fname = ''
lname = ''
age = ''
geo = ''

while name != 'quit':
      print("--- Who is eligible to vote --- ")
      fname = input('Enter first name: ')
      lname = input('Enter last name: ')
      geo = input("Enter where you're from: ")
      age = int(input('Enter age: '))
      if age >= 18:
            print('Elgible to vote')
      elif geo == 'jeremie' or geo == 'Jeremie':
            print('You are from Grand-Anse')
      else:
            print('Not eligible to vote! ')
            break
            

