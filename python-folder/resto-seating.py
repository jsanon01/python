# This script is about Restaurant Seating
# while + if-else statment for a dinner group


while True:
    user = int(input('How many people are there?: '))

    if user > 8:
        print('You are on the waiting list!')
    else:
        print('There is a table ready!')
