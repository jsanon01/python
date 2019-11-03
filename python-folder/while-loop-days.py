# This script prints wile-loop with if-elif statement

day = input('Enter a day: ').lower()

q = ''

while day != 'q':
      
      if day == 'monday':
            print('Happy Monday!')
      elif day == 'tuesday':
            print('Happy Tuesday')
      elif day == 'wednesday':
            print('Happy Wednesday')
      elif day == 'thursday':
            print('Happy Thursday')
      elif day == 'friday':
            print('Happy Friday')
      elif day == 'saturday':
            print('Happy Saturday')
      elif day == 'sunday':
            print('Happy Sunday')
      else:
            print('You have entered a wrong day!')
      print('Enter q for quit: ')
      day = input('Enter a day: ').lower()
      

print('You have asked to exit the loop!')
