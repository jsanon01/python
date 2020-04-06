"""
I want to define a class named quadriateral
I want to define __init__ function with the values: a, b, c, and d
I want to define a function inside the class named perimeter
I want to instantiate an object named roro with tne class 'quadrilateral'
I want to print the object named roro

"""
perimeter = ''

class quadrilateral:
    def __init__(self, a, b, c, d):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d

    def perimeter(self):
        p = self.side1 + self.side2 + self.side3 + self.side4
        print('\nThe perimeter is: {}'.format(p))

roro = quadrilateral(10, 20, 10, 20)

roro.perimeter()

print(perimeter)























































"""
perimeter = ''

class quadriLateral:
    def __init__(self, a, b, c, d):
        self.roro1 = a
        self.roro2 = b
        self.roro3 = c
        self.roro4 = d

    def perimeter(self):
        p = self.roro1 + self.roro2 + self.roro3 + self.roro4
        print('perimeter is: {}'.format(p))

q1 = quadriLateral(20, 15, 20, 14)

q1.perimeter()

print(perimeter)
"""
