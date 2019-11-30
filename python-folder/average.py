# This script prints the average of 2 numbers

score1 = int(input('Enter first number: '))

score2 = int(input('Enter second number: '))
score = ''

while score != 'q':
    average = (score1 + score2) // 2

    print(f'The average of {score1} and {score2} is {average}')
    score1 = int(input('Enter first number: '))
    score2 = int(input('Enter second number: '))
