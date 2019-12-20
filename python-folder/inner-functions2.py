# This script prints inner and outer functions

print()

def operations():

    num1 = int(input('Enter 1st number: '))

    num2 = int(input('Enter 2nd number: '))
    result = num1 + num2
    result = num1 - num2
    result = num1 * num2
    result = num1 / num2

    def add():
#        result = num1 + num2
        print('Addition: {} + {} = {}'.format(num1, num2, result))
    add()


    def sub():
#        result = num1 - num2
        print('Substraction: {} - {} = {}'.format(num1, num2, result))
    sub()        


    def mul():
#        result = num1 - num2
        print('Multiplication: {} - {} = {}'.format(num1, num2, result))

    mul()


    def div():
#        result = num1 / num2
        print('Division: {} / {} = {}'.format(num1, num2, result))
    div()


operations()

