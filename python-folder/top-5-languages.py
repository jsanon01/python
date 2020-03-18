"""
I want to create a function named ruby
I want to create a function named swift
I want to create a function named java
I want to create a function named python
I want to create a function named javascript
I want to create a function named market
I want to create a function named employers

I want to create a main function named main with a while statement:
- to exit when x = 0
- to call javascript when x = 1
- to call python when x = 2
- to call java when x = 3
- to call swift when x = 4
- to call ruby when x = 5
- to call the market when x = 6
- to call the employers when x = 7

"""

def ruby():
    print("\n'ruby on rails' is suitable framewok for building websites".title())

def swift():
    print('\nswift is the primary language for building ios apps: iphones, ipads.\nthe downsize is not really a cross-platform language...'.title())

def java():
    print('\njava is one of the most powerful and widely used languages.\njava can also be used for creating android apps and websites...\nunfortunately it is not the easiest language to learn...'.title())

def python():
    print('\npython is suitable for data seciences and machine learning.\nyou can create websites with django and flask frameworks.\nmoreover, python is popular at both small and larger companies.'.title())

def javascript():
    print('\njavascript is often run on web browsers.\nrecently people start using javascript to create backend codes\nrunning on servers.also it is a language that is easy to learn.'.title())

def market():
    print('\npython and javascript are more suitable for beginners.\n1. interested in ui and animations, javascript is of essence.\n2. python is for user interface, and data sciences.\n3. java is more for advanced computing.\n4. swift is for ios devices.\n5. ruby is for web frameworks. '.title())

def employers():
    print('\nemployers are looking for:\n- coding skils\n- problem solving\n- data structures and algorithms'.title())

print('\nHere are the 5 top programming languages in the markeplace:'.upper())

print('\n[0] Quit\t[1] Javascript\t[2] Python\t[3] Java\t[4] swift\n[5] Ruby\t[6] market\t[7] employers'.title())

def main(): 
    x = int(input('Enter a number from 0 - 7: '))
    while x:
        if x == 1:
            javascript()
        elif x == 2:
            python()
        elif x == 3:
            java()
        elif x == 4:
            swift()
        elif x == 5:
            ruby()
        elif x == 6:
            market()
        elif x == 7:
            employers()
        else:
            print('invalid number')

        x = int(input('\nEnter a number from 0 -7: '))

    print('You have exited the script..!')

print()

main()

print()

