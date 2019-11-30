# This script prints a while-loop

age = int(input('Enter age: '))


while age != 'q':
#    print(age)
    if age >= 12 and age <= 16:
        print('Your cost is $0')
    elif age <= 17:
        print('Your cost is $5')
    elif age >= 18 and age <=  62:
        print('Your cost is $20')
    elif age >= 63 and age <= 90:
        print('Discount must be applied!')
    else:
        print('Free Admission for elderly!')
    print('enter q for quit: ')
    age = int(input('Enter age: '))
