#!/usr/bin/

# hour calculation

print('--------------------------------------------------------------------')

print("This script greets you 'Good Morning, Afternoon, and Evening', accordingly...")

print()

hour = int(input('Enter hour in format [0 -24]: '))

if hour >= 1 and hour < 12:
    print()
    print('Good morning!')

elif hour >= 12 and hour < 18:
    print()
    print('Good afternoon')

elif hour >= 18 and hour < 24:
    print('Good evening')

else:
    print()
    print('Wrong format | More than 24-hour!')

print()
