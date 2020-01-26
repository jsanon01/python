"""
I want to ask the user for its first name
I want to ask the user for its last name
I want to ask the user for its phone number
I want the program to save name and phone number in a given file

"""
import csv

print("\nThis script prints out name and phone in a text file.")

fname = input('Enter first name: ')

lname = input('Enter last name: ')

phone = input('Enter a number: ')


f = open('jodel.txt', 'w')

print()

f.write("First Name\tLast Name\tPhone\n")

f.write('---------------------------------------------')

f.write('\n{}\t\t'.format(fname).title())

f.write('{}\t\t'.format(lname).title())

f.write('{}\t\t\t'.format(phone).title())

f.write('\t\t\t')


f.close()

f = open('jodel.txt', 'r')

data = f.read()

f.close()

print(data)

print()
