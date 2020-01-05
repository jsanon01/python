from urllib.request import urlopen



print('\n------ Ths script prints text file from a website ------')

print()

with urlopen("http://sixty-north.com/c/t.txt") as story:

    for line in story:

#        print(f"{line.decode('utf-8')}") # good line of code

        print(f"{line.decode('utf-8').title()}")

print()
