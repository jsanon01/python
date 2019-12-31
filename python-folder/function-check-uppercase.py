# This script double checks if a word is Uppercase in a function

user_input = 'Enter a word: '

print()

print('This script double checks if a word is "Uppercased" in a function: ')

def function():

    word = input(user_input)

    if word == word.upper():

        print('True... {} is uppercased'.format(word))

    else:

        print('False...{} does not meet the requirement!'.format(word))

function()

print()
