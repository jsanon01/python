"""
I want to print a function 'Dept of Grand-Anse'
I want to print a function 'Capital of Grand-Anse'
I want to print a function 'Major cities of Grand-Anse'
I want to print a function 'Major towns of Grand-Anse'
I want to print a function 'Famous people in Grand-Anse'

I want a main function to call: dept(), capital(), cities(), towns(), people()
I want 'Dept of Grand-Anse' to be called when x = 1 in the main function
I want 'Capital of Grand-Anse' to be called when x = 2 in the main function
I want 'Major Cities of Grand-Anse' to be called when x = 3 in the main function
I want 'Major towns of Grand-Anse' to be called when x = 4 in the main function
I want 'Famous people of Grand-Anse' to be called when x = 5 in the main function

"""
print()

def dept():
    print('Grand-Anse Dept is located in Southern west side of Haiti.')

#dept()

def capital():
    print("\nThe capital of Grand-Anse Dept is Jeremie aka 'The city of Poetry...'")

#capital()    

def cities():
    print("\nThe major cities of Grand-Anse Dept are:\nJeremie\t\tAnse-Dainault\t\tDame-Marie\tLes Irois\nAbricots\tMarfranc\t\tMoron\t\tChambellan\nCorail\t\tPestel\t\t\tBeaumont...")

#cities()

def towns():
    print("\nThe towns are:\nJeremie\t\tLeon\tFond-Cochon...")

def people():
    print("\nThe Famous people are:\netzer vilaire\t\tjean briere\t\tedmond laforest\nlesly center\t\teddy rene\t\twifrid simeon\ngary rouzier\t\tpatrick moussignac\tLes Cedras...")

print('This script prints Grand-Anse Geo areas & Famous People through a main loop.\n[1] Dept\t\t[2] Capital\t[3] Cities\t[4] Towns\n[5] People\t\t[0] Quit: ')

def main():
    x = int(input('\nEnter a number from 0 - 5: '))
    
    while x:

        if x == 1:
            dept()
        elif x == 2:
            capital()
        elif x == 3:
            cities()
        elif x == 4:
            towns()
        elif x == 5:
            people()
        else:
            print('Invalid Number!')
        x = int(input('Enter a number from 0 - 5: '))

    print('\nYou have exited the script.')

main()

print()
