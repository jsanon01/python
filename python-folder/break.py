# Break statement

number = 0
print('Statement will BREAK at 7')
for number in range(0, 10):
    if number == 7:
        break; # statement will break here
    else:
        print(f'Number is ' + str(number))
