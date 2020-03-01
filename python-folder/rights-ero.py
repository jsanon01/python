"""
I want to define a class method called event
I want to define a class method called response
I  want to define a class method called outcome

I want to define a main function called ERO() with a while statement
- event  will be called when x = 1
- response will be called when x = 2
- outcome will be called when x = 3
- speech will be called when x = 4
- pic will be called when x = 5
- web will be called when x = 6


"""
from PIL import Image
import  webbrowser

print()

print("The Empowering Equation for Work and Life.")

print('\nEvent + Response = Outcome')

print("\n[0] Quit\t [1] Event\t [2] Response\t [3] Outcome\n[4] Speech\t [5] Pic\t [6] Website ")

def event():
    print("\nevent is an occurrence or something that is not changeable\nlike 'time and tide...'.")

def response():
    print('\nresponse is a decision-making either fight or flight to an event')

def outcome():
    print('\noutcome is a twofold consequence: positive or negative')

def speech():
    print("\nIn the log run, we shape our lives, and we shape ourselves.\nThe process never ends until we die. And the choices we make\nare ultimately our own responsibility.\n\t\t\t\t\tEleanor Roosevelt")

original = Image.open('ero_pic.png')


def main():
    x = int(input('\nEnter a number from 0 - 6: '))
    while x:
        if x == 1:
            event()
        elif x == 2:
            response()
        elif x == 3:
            outcome()
        elif x == 4:
            speech()
        elif x == 5:
            original.show()
        elif x == 6:
            webbrowser.open_new_tab('https://www.habitsforwellbeing.com/event-response-outcome-an-empowering-equation-for-work-and-life/')
        else:
            print('Invalid number...')

        x = int(input('\nEnter a number from 0 - 4: '))

main()

print('\nExiting the script')

print()
