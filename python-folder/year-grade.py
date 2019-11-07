# This script prints a while-loop with if-elif statement 

year = " "

while year != 'q':

    year = input('Enter a grade from 0 - 13 or q to quit: ')

    if year.isdigit():
        year = int(year)
        if year == 0:
            print('You are in Pre-School')
        elif year == 1:
            print('You are in Kindergarten')
        elif year == 2:
            print('You are in 1st Grade')
        elif year == 3:
            print('You are in 2nd Grade')
        elif year == 4:
             print('You are in 3rd Grade')
        elif year == 5:
            print('You are in 4th Grade')
        elif year == 6:
            print('You are in 5th Grade')
        elif year == 7:
            print('You are in 6th Grade')
        elif year == 8:
            print('You are in 7th Grade')
        elif year == 9:
            print('You are in 8th Grade')
        elif year == 10:
            print('You are in 9th Grade or Freshman')
        elif year == 11:
            print('You are in 10th Grade or Sophomore')
        elif year == 12:
            print('You are in 11th Grade or Junior')
        elif year == 13:
            print('You are in 12th Grade or Senior')
        else:
            print('You entered an invalid entry')

