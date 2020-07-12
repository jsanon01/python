"""
I want to define a function named pascal()
I want to define a function named work()
I want to define a function named humain()
I want to define a function named divin()

I want to define main function named main()
I want to use 2 inputs functions for interaction
I want to use a while statement

"""

print('\n-------------------- Menu --------------------------')

print('\n[0] Quit  [1] Who?  [2] Work [3] Human [4] Divine')

print('\none of the greatest philosophers'.title())

def pascal():
    print('\nHis name is: Pascal Ide')
    print("- docror of philosophy\n- doctor of medicine\n- master of theology.".title())

def ouvrage():
    print("\nhere are some of his literary work: ".title())
    print("- 'know yourself better to love yourself' = 'mieux se connaitre pour mieux s'aimer".title())
    print("- 'working methodically is to succeed' = 'travailler avec methode c'est reussir''".title())
    print("- 'building your personality' = 'construire sa personnalite'".title())
    print("- 'knowing your heart' = 'connaitre ses blessures'".title())
    print("- 'body to heart' = 'le corps a coeur'".title())

def humain():
    print("\n'understand to love' = 'comprendre pour aimer'\n'live to love' = 'aimer pour vivre'\n'dancing is human' = 'danser est humain'".title())

def divin():
    print("\n'love to understand' = 'aimer pour comprendre'\n'love to live' = 'aimer pour vivre'\n'singing is divine' = 'chanter est divin'".title())


def main():
    x = int(input("\nEnter a number: "))
    while x:
        if x == 1:
            pascal()
        elif x == 2:
            ouvrage()
        elif x == 3:
            humain()
        elif x == 4:
            divin()
        else:
            print("\nInvalid number!")
        x = int(input("\nEnter a number: "))
    print('\nExiting the loop!')

main()

print()
