# This scrpit is about 2 control statements
# 1) for + if-else with a list

cars = ['kia', 'audi', 'bmw', 'ford']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print('=======================================')
# 2) for + if-elif-else with a list

students = ['joe', 'carla', 'peter', 'alex']

for student in students:
    if student == 'peter':
        print(student.upper())
    elif student == 'joe':
        print(student.title())
    else:
        print(len(student))
