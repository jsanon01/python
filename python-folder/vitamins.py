"""
I want to call a function named Vitamins
I want to call a function named Vitamin A
I want to call a function named Vitamin C
I want to call a function named Vitamin D
I want to call a function named Vitamin E
I want to call a function named Vitamin K
I want to call a function named Vitamin B1
I want to call a function named Vitamin B2
I want to call a function named Vitamin B3
I want to call a function named Vitamin B5
I want to call a function named Vitamin B6
I want to call a function named Vitamin B7
I want to call a function named Vitamin B9
I want to call a function named Vitamin B12

I want the main function to call all the subfunctions
I want a while loop inside the main function with the following info:
- while loop to exit when x = 0
- vitamin A to be called when x = 1
- vitamin C to be called when x = 2
- vitamin D to be called when x = 3
- vitamin E to be called when x = 4
- vitamin K to be called when x = 5
- vitamin B1 to be called when x = 6
- vitamin B2 to be called when x = 7
- vitamin B3 to be called when x = 8
- vitamin B5 to be called when x = 9
- vitamin B6 to be called when x = 10
- vitamin B7 to be called when x = 11
- vitamin B9 to be called when x = 12
- vitamin B12 to be called when x = 13

"""
from PIL import Image

print("\nThis script not only uses a while-statement\nbut also prints out a 'lis of vitamins': ")

print("\n[0]Quit\t[1] A\t[2] C\t[3] D\t[4] E\t[5] K\t[6] B1\n[7] B2\t[8] B3\t[9] B5\t[10] B6\t[11] B7\t[12] B9\t[13] B12\n[14] Metabo_pic: ")

def Vitamins():
    print('\nIn short, Vitamins are needed for normal cell function, growth, and development...\n')

def vitamin_A():
    print('Vitamin A')

def vitamin_C():
    print('Vitamin C')

def vitamin_D():
    print('Vitamin D')

def vitamin_E():
    print('Vitamin E')

def vitamin_K():
    print('Vitamin K')

def vitamin_B1():
    print('Vitamin B1')

def vitamin_B2():
    print('Vitamin B2')

def vitamin_B3():
    print('Vitamin B3')

def vitamin_B5():
    print('Vitamin B5')

def vitamin_B6():
    print('Vitamin B6')

def vitamin_B7():
    print('Vitamin B7')

def vitamin_B9():
    print('Vitamin B9')

def vitamin_B12():
    print('Vitamin B12')


original = Image.open('vita_pic.png')
	
def main():
    x = int(input('Enter a number from 0 - 13: '))
    while x:
        if x == 1:
            vitamin_A()
        elif x  == 2:
            vitamin_C()
        elif x == 3:
            vitamin_D()
        elif x == 4:
            vitamin_E()
        elif x == 5:
            vitamin_K()
        elif x == 6:
            vitamin_B1()
        elif x == 7:
            vitamin_B2()
        elif x == 8:
            vitamin_B3()
        elif x == 9:
            vitamin_B5()
        elif x == 10:
            vitamin_B6()
        elif x == 11:
            vitamin_B7()
        elif x == 12:
            vitamin_B9()
        elif x == 13:
            vitamin_B12()
        elif x == 14:
            original.show()
        else:
            print('You have entered an Invalid number. try again!'.title())
        x = int(input('Enter a number from 0 - 13: '))

Vitamins()

main()

print('You have exited the loop...!')

print()
