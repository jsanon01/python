"""
I want to define a function named add
I want to define a function named sub 

https://www.geeksforgeeks.org/polymorphism-in-python/

"""

print("\nThis script prints out the sum of a function:\ndef add(x + y + z = 0):\n\treturn x + y + z\n\nprint(add(2, 9))\nprint(add(2, 6, 9) ")
print()

def add(x, y, z = 0):
    return x + y + z

print("\nThis script prints out the difference of a function:\ndef add(x - y - z = 0):\n\treturn x - y - z\n\nprint(add(2, 9))\nprint(add(2, 6, 9) ")
def sub(x, y, z = 0):
    return x - y - z

print(add(2,9))
print(add(2,6,9))

print()

print(sub(12, 45))
print(sub(72, 39, 15))
print()
