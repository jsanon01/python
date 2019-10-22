# This script is about even number with while-loop

number = ''

prompt = 'Enter a number: '

while number != 'quit':
    number = int(input(prompt))
    if number %  2 == 0:
        print(f'{number} is an even number.')
    else:
        print(f'{number} is not an even number.')
    print("Type 'quit' to leave the loop...")
