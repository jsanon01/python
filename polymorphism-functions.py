"""
https://www.geeksforgeeks.org/polymorphism-in-python/

"""


def add(x, y, z = 0):
    return x + y + z

def sub(x, y, z = 0):
    return x - y - z

print(add(2,9))
print(add(2,6,9))

print()

print(sub(12, 45))
print(sub(72, 39, 15))
