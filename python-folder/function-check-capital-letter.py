# This script double checks if a word starts with Capital letter

user_input = 'Enter a word: '


print('This script double checks if a word starts with Capital letter')

def function():

    word = input(user_input)

    if word == word.capitalize():

        print('True...{} is capitalized.'.format(word))

    else:

        print('False...{} is not capitalized.'.format(word))

function()
