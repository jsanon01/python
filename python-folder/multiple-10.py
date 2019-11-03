# This script is about while loop printing multiple of 10


number = ''

prompt = 'Enter a number: '

while number  != 'quit':
    number = int(input(prompt))
    if  number % 10 == 0:
        print(f'{number} is a multiple of 10: ')
    else:
        print('Number can not be divided by 10.')

