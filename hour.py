#!/usr/bin/

# hour calculation

print("This script greets you 'Good Morning, Afternoon, and Evening, accordingly...'")

hour = int(input('Enter hour [0 -24]: '))

if hour >= 1 and hour < 12:
    print('Good morning')

elif hour >= 12 and hour < 18:
    print('Good afternoon')

elif hour >= 18 and hour < 24:
    print('Good evening')

else:
    print('Wrong format | More than 24-hour!')
