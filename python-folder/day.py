# This script prints a while-loop including an if-elif statement

day = input('Enter day: ').lower()

while day != 'q':

    if day == 'monday':
        print('Happy Monday ....Moody Monday')
    elif day == 'tuesday':
        print('Happy Tuesday .... Thrifty Tuesday!')
    elif day == 'wednesday':
        print('Happy Wednesday .... Wacky Wednesday!')
    elif day == 'thursday':
        print('Happy Thursday .... Thirsty Thursday!')
    elif day == 'friday':
        print('Happy Friday .... Funny Friday!')
    elif day == 'Saturday':
        print('Happy Saturday .... Sacred Saturday!')
    elif day == 'sunday':
        print('Happy Sunday .... Sunny Sunday!')
    else:
        print('Wrong Day!')
    print('Enter q for quit')
    day = input('Enter a day: ').lower()
