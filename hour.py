#!/bin/bash

# hour calculation

hour = int(input('Enter hour: '))

if hour >= 1 and hour < 12:
    print('Good morning')

elif hour >= 12 and hour < 18:
    print('Good afternoon')

elif hour >= 18 and hour < 24:
    print('Good evening')

else:
    print('Wrong format | More than 24-hour!')
