#!/usr/bin/python

print()

print('This script counts words form another script')

file=open("haitian-tvs.txt","r+")

wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print()

print('--------------------------------------------------------------')

print()

#print('This script counts words form another script')

for k, v in wordcount.items():
	print(k, v)
#print (f'{word}\t,{wordcount}')

file.close();
