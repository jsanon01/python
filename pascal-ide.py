"""


"""
print('\npascal ide is a: '.title())

def pascal():
    print("\n- docror of philosophy\n- doctor of medicine\n- master of theology.".title())

def ouvrage():
    print("\nhere are some of his literary work: ".title())
    print("- 'know yourself better to love yourself' means 'mieux se connaitre pour mieux s'aimer".title())
    print("- 'working methodically is to succeed' means 'travailler avec methode c'est reussir''")
    print("- 'building your personality' means 'construire sa personnalite'")
    print("- 'knowing your heart' means 'connaitre ses blessures'")
    print("- 'body to heart' means 'le corps a coeur'")

def humain():
    print("'understand to love' means 'comprendre pour aimer'\n'live to love' means 'aimer pour vivre'\n'dancing is human' means 'danser est humain'".title())

def divin():
    print("'love to understand' means 'aimer pour comprendre'\n'love to live' means 'aimer pour vivre'\n'singing is divine' means 'chanter est divin'")


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
            print("\nInvalid number")
        x = int(input("\nEnter a number: "))
    print('\nExiting the loop!')

main()

print()
