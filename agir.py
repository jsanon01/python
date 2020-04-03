"""
I want to define a function named a
I want to define a function named g
I want to define a function named i
I want to define a function named r
I want to open a website  named webbrowser
I want to define a function named metro

I want to define a main function named agir including a while statement 
- to quit when x = 0
- to call a() when x = 1
- to call g() when x = 2
- to call i() when x = 3
- to call r() when x = 4
- to call webbrowser when x = 5
- to call metro when x = 6

"""
import webbrowser

print('\n<<Beaucoup personnes ont des reves, ceux qui reussissent ont des objectifs.>>\n\t\t\t\t\t\t\t\tThami Kabbaj')

print('\n[0] Quit [1] A\t[2] G\t[3] I\t[4] R\t[5] Web Reference\n[6] Metro')

def a():
    print("\n'A' pour Apprendre")

def g():
    print("\n'G' pour Gagner plus")

def i():
    print("\n'I' pour Investir")

def r():
    print("\n'R' pour Reussir, Retraite, Repos, ou Reves")

def metro():
    print("\nMetro-Boulot-Dodo va au detriment de la liberte financiere de l'homme...\n")
    print("La liberte financiere permet d'arreter d'echanger son temps contre un salaire\net d'avoir plus de temps a consacrer a sa famille et a ses proches.\n\nLa liberte financiere est d'avoir la possibilite de ne plus subir la rountine\nMetro-Boulot-Dodo.")

def agir():
    x = int(input('\nEnter a number from 0 - 6: '))

    while x:
        if x == 1:
            a()
        elif x == 2:
            g()
        elif x == 3:
            i()
        elif x == 4:
            r()
        elif x == 5:
            webbrowser.open('https://www.amazon.com/AGIR-virer-patron-quitter-banquier/dp/2212571321')
        elif x == 6:
            metro()
        else:
            print('\nInvalid number')

        x = int(input('\nEnter a number from 0 - 6: '))

    print('\nExiting the script')

agir()

print()
