# This script is about a while-loop with Boolean (True)

prompt = 'Enter a name: '

while True:
    name = input(prompt)

    if name == 'quit':
        break
    else:
        print(f'{name.title()} are you a registered voter?')
