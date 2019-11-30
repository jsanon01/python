# Thi script prints out the list of available courses

print()

course = ''

print('This script prints out the list of codified courses')

while course != 'q':
    
    course = input("Enter the course's code form 1 - 3 or 'q' for exit: ")

    if course.isdigit():

        course = int(course)

        if course == 1:
 
           print('A & P is available during Summer Time')

        elif course == 2:

            print('Math is available during Summer Time')

        elif course == 3:

            print('Chemistry is available during Summer Time')

        else:

            print('This course is not offered during Summer Time!')

print()
