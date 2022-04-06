"""
I want to define a function named def
I want to create a switch statement inside the function
I want to define a while loop and if statement inside
I want to print out the function
"""
print('\n---------- menu ----------'.upper())

print('\n[1] r [2] o [3] s [4] e'.upper())

def rose(roz):
    switcher= {
	1: "\nr --> stands for 'respect'".title(),
	2: "\no --> stands for 'ownership'".title(),
	3: "\ns --> 'superior service'\n\nto exhibit an attitude in which all requests are considered reasonable".title(),
	4: "\ne --> 'excellence'\n\nto exceed the expectations by achieving optional outcones".title()
	}
    return switcher.get(roz, '\nInvalid number')

kiki = ''

result = ''

while kiki != 'q':
    if kiki.isdigit():
        result = rose(int(kiki))
    print(result)
    print()
    kiki = input("Enter 1 - 4 or 'q' to quit:  ")

print()

