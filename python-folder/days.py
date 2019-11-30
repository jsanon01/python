# This script prints a while-loop with if-elif statement


day = input('Enter a day (out): ').lower()

while day != 'q':

    if day == 'monday':
        print('Happy Monday .... Moody Monday!')
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
        print('You have entered a wrong date')

    # print(day)
    print("Engter q to quit")
    day = input('Enter a Day (in): ').lower()

print("You have exited the loop...")
