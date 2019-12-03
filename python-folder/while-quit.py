# This script is about a while-loop
# it will stop when typing 'quit'

message = ''

prompt = "Please tell me something or 'q': "

while message != 'q':

    message = input(prompt)

    print(f'You have entered {message.title()}')
