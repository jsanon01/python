# This script is about an infinite loop using while True statement

while True:
      number = int(input('Enter a number: '))
      if number > 18:
            print('Eligible to smoke')
      elif number >= 21:
            print('Eligible to drink and smoke')
            break
      else:
            print('Not eligible to smoke nor drink')
