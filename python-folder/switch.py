# This script prints a while-loop with if-elif statement 

def week(school):
        switcher = {
            0:'You are in Pre-School',
            1:'You are in Kindergarten',
            2:'You are in 1st Grade',
            3:'You are in 2nd Grade',
	        4:'You are in 3rd Grade',
            5:'You are in 4th Grade',
            6:'You are in 5th Grade',
            7:'You are in 6nd Grade',
	        8:'You are in 7th Grade',
            9:'You are in 8th Grade',
            10:'You are in 9th Grade',
            11:'You are in 10th Grade',
            12:'You are in 11th Grade',
            13:'You are in 12th Grade',
   
        }
        return switcher.get(school,"Invalid Grade")

year = " "

while year != 'q':
    if year.isdigit(): # '1'.digit() 'w'.isdigit() 'karlo'.isdigit()
        result = week(int(year))
        print(result)
    year = input('Enter a number from 0 - 13 or q to quit: ')
