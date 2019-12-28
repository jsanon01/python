# This script prints out a function along with 'Ternary Operator'

print("\nThis script prints out a function along with 'Ternary Operator'")

print()

def searchList(aList, el):

    if el in aList:

        return True

    else:

        return False

result = searchList(['one', 2, 'three'], 2)

print('The result is: {}'.format(result))

print()
