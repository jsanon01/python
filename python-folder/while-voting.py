# This script is about a while-loop with Boolean (True)


print("Using this script, type 'q' for exit the loop!")

prompt = 'Enter first + last names: '

while True:

    name = input(prompt)

    if name == 'q':
       
         break
 
    else:
            print(f'{name.title()} are you a registered voter?')
