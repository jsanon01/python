"""
I want to create 15 functions (step_1 - step_15)
I want to create a main function along with a  while statement


"""
print("\n'the save the cat beat sheet' is a roadmap which means\na series of road markers preventing aimlessly roaming.".title())
print('\n-------- here are the 15-step process -------'.title())
print('\n[1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15]')
print('\n-------- here is the 3-act structure wrapping the 15-step --------'.title())
print('\n[31] setup [32] conflict [33] resolution'.title())

def step_1():
    print('step 1 --> opening image'.title())

def step_2():
    print('step 2 --> setup '.title())

def step_3():
    print('step 3 --> theme stated'.title())

def step_4():
    print('step 4 --> catalyst'.title())

def step_5():
    print('step 5 --> debate'.title())

def step_6():
    print('step 6 --> break into two'.title())

def step_7():
    print('step 7 --> b story'.title())

def step_8():
    print('step 8 --> fun & games'.title())

def step_9():
    print('step 9 --> midpoint'.title())

def step_10():
    print('step 10 --> bad guy close-in'.title())

def step_11():
    print('step 11 --> all is lost'.title())

def step_12():
    print('step 12 --> dark night of the soul'.title())

def step_13():
    print('step 13 --> break into three'.title())

def step_14():
    print('step 14 --> finale'.title())

def step_15():
    print('step 15 --> final image'.title())

def setup():
    print('\nsetup --> '.title())

def conflict():
    print('\nconflict --> '.title())

def resolution():
    print('\nresolution --> '.title())

def main():
    x = int(input('\nEnter a number from 0 - 15 || 31 -33: '))
    while x:
        if x == 1:
            step_1()
        elif x == 2:
            step_2()
        elif x == 3:
            step_3()
        elif x == 4:
            step_4()
        elif x == 5:
            step_5()
        elif x == 6:
            step_6()
        elif x == 7:
            step_7()
        elif x == 8:
            step_8()
        elif x == 9:
            step_9()
        elif x == 10:
            step_10()
        elif x == 11:
            step_11()
        elif x == 12:
            step_12()
        elif x == 13:
            step_13()
        elif x == 14:
            step_14()
        elif x == 15:
            step_15()
        elif x == 31:
            setup()
        elif x == 32:
            conflict()
        elif x == 33:
            resolution()
        else:
            print('\nInvalid number...')
        x = int(input('\nEnter a number from 0 - 15 || 31 -33: '))

    print('\nYou have exited the script...')

main()

print()

