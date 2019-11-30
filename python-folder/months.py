# This script prints the monts of the year using a swicther

def months(year):

    switcher = {
	
	1: 'January is the 1st Month of the Year!',
	2: 'February is the 2nd Month of the Year! ',
	3: 'March is the 3rd Month of the Year! ',
	4: 'April is the 4th Month of the Year! ',
	5: 'May is the 5th Month of the Year! ',
	6: 'June is the 6th Month of the Year!  ',
	7: 'July  is the 7th Month of the Year!',
	8: 'August is the 8th Month of the Year! ',
	9: 'September is the 9th Month of the Year! ',
	10: 'October is the 10 Month of the Year! ',
	11: 'November is the 11th Month of the Year! ',
	12: 'December is the 12th Month of the Year! ',
	
	}
    return switcher.get(year, 'Invalid entry for months!')

years = ''

while years != 'q':
    if years.isdigit():
        result = months(int(years))
        print(f'{result}')
    years = input('Enter a number from 1 - 12 or q to exit the loop: ')

