"""
I want to ask the user for its name
I want to ask the user for its phone number
I want the program to save name and phone number in a given file

"""
import csv

print("\nThis script prints out name and phone in a text file.")

name = input('Enter name: ')

phone = input('Enter a number: ')


f = open('jodel.txt', 'w')

f.write("Name\t\t\tPhone\n")
f.write('{}\t\t'.format(name).title())
#f.write(' ')
f.write('{}\t\t\t'.format(phone).title())
f.write('\t\t\t')


f.close()


f = open('jodel.txt', 'r')

data = f.read()

f.close()

print(data)

print()
