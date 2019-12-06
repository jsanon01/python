# This script prints age group


print('This script prints Age Group')

age = ''

while age != 'q':

    age = input('Enter age: ')

    if age.isdigit():

        age = int(age)

        if age >= 0 and age <= 12:

            print('Kid...')

        elif age >= 13 and age <= 19: 

            print('Teenager...')

        elif age >= 20 and age <= 30:

            print('Young Adult ...')

        elif age >= 31 and age <= 64:

            print('Adult...')

        elif age >= 65 and age <= 120:

            print('Senior ...')

        else:

            print('Inavlid Entry ...')


print('You have exited the loop...')
