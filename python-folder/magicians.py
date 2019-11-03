# This script prints list and copies of list

magicians = ['alice', 'bob', 'david', 'carolina'] # list

copy_magicians = magicians.copy()

print(magicians)

print(copy_magicians)

copy_magicians.append('Pascal')

print(magicians)

print(copy_magicians)

copy_magicians2 = copy_magicians[:]

print(copy_magicians2)

print()

first_name = 'karlo' # string

age = 21 # integer

print(first_name.upper())

magicians.sort()

for magician in magicians:
    print(magician.title())
print(len(magicians))

print('========')

