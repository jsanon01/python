# This script enlists people by asking names and age
# using not only a while-loop but also break statement

message = ''

prompt = 'Tell me more about you: '


while message != 'quit':
      message = input(prompt)
#      print(message.title())
      if message == 'quit':
            break
      age = int(input(f'{message.title()}, please enter your age: '))
      if age >= 18:
            print(f'{message.title()}, you are eligible to vote...')
      else:
            print(f'{message.title()}, you are not eligible to vote...')
