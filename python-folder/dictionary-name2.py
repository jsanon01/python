



class_list = dict()

#data = input('Enter name & age separated by ":" ')
while True:
    names = input('Enter names and age separated by ":" : ')
    if names == 'q':
        break

    temp = names.split(':')

    class_list[temp[0]] = int(temp[1])
 
    # Displaying the dictionary
    for key, value in class_list.items():
        print('Name: {}\nAge: {}'.format(key, value).title())

