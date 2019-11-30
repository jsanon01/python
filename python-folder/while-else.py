# This script is about while-else loop
# which is a condition-controlled loop


prompt = 'What is your name: '

while True:
    kiko = input(prompt)

    if kiko == 'quit':
        break 
    else:
        print(f'My name is {kiko.title()}')

