
def rose(roz):
    switcher= {
	1: "r --> stands for 'respect'",
	2: "o --> stands for 'ownership'",
	3: "s --> 'superior service'",
	4: "e --> 'excellence'"
	}
    return switcher.get(roz, 'Invalid number')

kiki = ''

result = ''

while kiki != 'q':
    if kiki.isdigit():
        result = rose(int(kiki))
    print(result)
    kiki = input("Enter 1 -4 or 'q' to quit:  ")

print()
    
