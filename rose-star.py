"""
I want to define 4 functions respectively:
- r() - o() - s()  - e()

I want to define main function including a while loop

"""

print('\n---------- The STAR Philosophy ----------')


print('\n[11] S [12] T [13] A [14] R ')

def situation():
    print('situation')

def task():
    print('task')

def action():
    print('action')

def result():
    print('result') 

print('\n---------- The ROSE Philosophy ----------')

print('\n[1] R [2] O [3] S [4] E ')

def r():
    print("\nR stands for 'RESPECT'\n\nR means exhibits integrity, trust, and courtesy to fellow employees. ")

def o():
    print("\nO stands for 'OWNERSHIP'\n\nO means remains accountable to our clients' core values. ")

def s():
    print("\nS stands for 'Superior Service'\n\nS means exhibits an attitude in which all requests are considered reasonable. ")


def e():
    print("\nE stands for 'EXCELLENCE'\n\nE means meets or exceeds the expectations by achieving optional outcomes. ")

def main():

    x = int(input('\nEnter a number from 0 - 4: '))

    while x:
        if x == 1:
            r()
        elif x == 2:
            o()
        elif x == 3:
            s()
        elif x == 4:
            e()
        elif x == 11:
            situation()
        elif x == 12:
            task()
        elif x == 13:
            action()
        elif x == 14:
            result()
        else:
            print('\nInvalid number...')

        x = int(input('\nEnter a number from 0 - 4: '))

    print('\nYou have exited the script.')

main()

print()
