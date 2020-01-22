

f = open('roku.txt', 'w+')

f.write('\nConstat de caducite du Parlement Haitien:\nLe Lundi 13 Janvier 2020')

f.close()

f = open('roku.txt', 'r')

data = f.read()

f.close()

print(data)

print()
