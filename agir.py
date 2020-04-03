"""
I want to define a function named a
I want to define a function named g
I want to define a function named i
I want to define a function named r

I want to define a main function agir

"""

def a():
    print("'A' pour Apprendre")

def g():
    print("'G' pour Gagner plus")

def i():
    print("'I' pour Investir")

def r():
    print("'R' pour Reussir, Retraite, Repos, ou Reves")

def agir():
    x = int(input('enter a letter: '))

    while x:
        if x == 1:
            a()
        elif x == 2:
            g()
        elif x == 3:
            i()
        elif x == 4:
            r()
        else:
            print('invalid number')

        x = int(input('enter a letter: '))
    print('exiting the script')

agir()

print()

