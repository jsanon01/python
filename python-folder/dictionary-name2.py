"""
I want to create an empty dictionary
I want to use a while loop statement with the following:
- input
- a break statement using if 
- split the input 

I want to dislay key-value pairs of the dictionary using for-loop

"""

class_list = dict()

print('\nThis script prints out names and age separated by ":" ')

while True:
    names = input('Enter names and age separated by ":" : ')
    if names == 'q':
        break

    temp = names.split(':')

    class_list[temp[0]] = int(temp[1])
 
    # Displaying the dictionary
    for key, value in class_list.items():
        print('Name: {}\nAge: {}'.format(key, value).title())

print()
