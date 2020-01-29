"""
I want to print a sorted list using 2 methods

"""

list = [9,6,3,1,4,8,0]

print('\nThis script sorts a list using 2 different methods: ')
print("\nOriginal lsit: list = [9,6,3,1,4,8,0]")
 
list.sort()

print("\n1st method is 'list.sort()': {}".format(list))

print()

print(f"\n2nd method is 'sorted(list)': {sorted(list)}")

print()
