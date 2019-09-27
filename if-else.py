cars = ['kia', 'audi', 'bmw', 'ford']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print('===============')
students = ['joe', 'carla', 'peter', 'alex']

for student in students:
    if student == 'peter':
        print(student.upper())
    elif student == 'joe':
        print(student.title())
    else:
        print(len(student))
