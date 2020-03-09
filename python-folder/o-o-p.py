""""
I want to define a function called oop
I want to define a function called class
I want to define a function called instans
I want to define a function called methods

I want to define a main function

"""
print('\nOOP is not just supported by Python, but it is a part of its very core.')

def oop():
    print("object oriented programming 'is all about code reuse'")

def klass():
    print('1) we define class: class():')

def instans():
    print('2) we create instances')

def methods():
    print('instances use methods defining in the class')

def main():
    x = int(input('\nEnter inputs: '))
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
        x = int(input('\nEnter inputs: '))

main()

print('You have exited the script...')

print()
