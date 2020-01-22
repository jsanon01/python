"""
I want to create a text file 'roku' and write in it
- to insert 2 new lines
- to close it
I want to open this text file 'roku'
I want to read its content
I want to print it out

"""

f = open('roku.txt', 'w+')

f.write('\nConstat de caducite du Parlement Haitien:\nLe Lundi 13 Janvier 2020')

f.close()

f = open('roku.txt', 'r')

data = f.read()

f.close()

print(data)

print()
