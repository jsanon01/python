import csv

print()

# Script writes 'csv file'

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
