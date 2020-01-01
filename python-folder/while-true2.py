# This script is about While-True loop which emphasizes break statement


print()

print('This script prints out while-true loop using a break statement')

prompt = "Guess a letter / word or 'q' to exit: "

while True:

    game = input(prompt)

    if game == 'q':

        break

    else:

        print(f"You entered {game.title()}")

print()
