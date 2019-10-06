# This script is about file-opening
# where pi-digit.txt is the file to open

with open('pi-digit.txt') as file_object:
    contents = file_object.read()
    print(contents)
