"""
I want to print import csv
I want to write in a given file (rtg.txt) by using command 'with open following mode=w' 
I want to read the file

"""
import csv

# Script writes 'csv file'

print("\nThis script not only writes into a file named 'rtg.txt' but also reads it.")

with open('rtg.txt', mode='w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['Name', 'City'])
    writer.writerow(['Amos Antoine', 'Jeremie'])
    writer.writerow(['Jean Madichon', 'Cayes'])
    writer.writerow(['Jean Tatoune', 'Gonaives'])


# Script reads 'csv file'

with open('rtg.txt', mode='r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)

print()
