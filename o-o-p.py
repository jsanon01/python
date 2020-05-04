""""
I want to define a function called oop
I want to define a function called class
I want to define a function called instans
I want to define a function called methods

I want to define a main function that will
- have a condition statement with while loop
- exit the loop when x = 0
- call oop() when x = 1
- call klass() when x = 2
- call instans() when x = 3
- call methods() when x = 4

"""
print('\nOOP is not just supported by Python, but it is a part of its very core.')

print('\n[1] OOP [2] Class [3] Instances\t [4] Methods')

def oop():
    print("object oriented programming 'is all about code reuse'")

def klass():
    print('1) we define class:\t "class A:" ')
#    print()
def instans():
    print('2) we create instances')

def methods():
    print('instances use methods defining in the class')

def main():
    x = int(input('\nEnter a number from 0 - 4: '))
    while x:
        if x == 1:
            oop()
        elif x == 2:
            klass()
        elif x == 3:
            instans()
        elif x == 4:
            methods()
        else:
            print('Invalid number..')
        x = int(input('\nEnter a number from 0 - 4: '))

main()

print('You have exited the script...')

print()
