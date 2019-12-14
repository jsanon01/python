# This scripts asks user to enter inputs and checks if word includes 'es'

word = 'best'
# word = ''
print()

print("This scripts asks user to enter inputs and checks if word 'best' includes... ")

name = ''

while name != 'q':

    if name == 'q':

        break

    name = input('Enter input: ')

    if 'es' in word:

        if name == 'es' or name == 'best':

            print('You got it right! The word you typed includes {}.'.format(word))

        else:

            print('Keep guessing!')


print('You have exited the loop!')
