"""
I want to define a class method called event
I want to define a class method called response
I  want to define a class method called outcome

I want to define a main class called ERO() with a while statemet
- event  will be called when x = 1
- response will be called when x = 2
- outcome will be called when x = 3
- speech will be called when x = 4
- pic will be called when x = 5
- web will be called when x = 3


"""
from PIL import Image
print("This script prints out a menu about an Equation.")
print("\n[0] Quit\t [1] Event\t [2] Response\t [3] Outcome\n[4] Speech\t [5] Pic\t [6] Website ")

def event():
    print("event is time-based..")

def response():
    print('response is either fight or fly')

def outcome():
    print('outcome is a twofold consequence: positive or negative')

original = Image.open('vita_pic.png')

def main():
    x = int(input('Enter a number from 0 - 4: '))
    while x:
        if x == 1:
            event()
        elif x == 2:
            response()
        elif x == 3:
            outcome()
        elif x == 4:
            original.show()
        elif x == 5:
            eleanor()
        else:
            print('Invalid number...')

        x = int(input('Enter a number from 0 - 4: '))

main()

print('\nExiting the script')

print()
