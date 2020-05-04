"""


"""

print('\n---------- The ROSE Philosophy ----------')

print('\n[1] R [2] O [3] S [4] E ')

def r():
    print("\nR stands for 'RESPECT'\n\nR means exhibits integrity, trust, and courtesy to fellow employees. ")

def o():
    print("\nO stands for 'OWNERSHIP'\n\nO means remains accountable to our clients' core values. ")

def s():
    print("\nS stands for 'Superior Service'\n\nS means exhibits an attitude in which all request are considered reasonable. ")


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
        else:
            print('\nInvalid number...')
        x = int(input('\nEnter a number from 0 - 4: '))
    print('\nYou have exited the script.')

main()

print()
