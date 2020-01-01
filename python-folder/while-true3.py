# This script prints out a while-true loop


words_to_yell = ''

print("\nThis script prints out a 'while-true loop'")

while True:

    if words_to_yell == 'q':
        break

    else:
        words_to_yell = input('Enter something: ')


    def yell_this(words_to_yell):
        print(f"You have entered: {words_to_yell.title()}")

    yell_this(words_to_yell)


print('\nYou have exited the script!')

print()


