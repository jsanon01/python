# This script prints a printing receipt

# Defining 3 items (variables) in 1 line each

p1_name, p1_price = 'Books', 49.75

p2_name, p2_price = 'Computer', 579.99

p3_name, p3_price = 'Monitor', 124.89

total =  p1_price + p2_price + p3_price


company_name = 'coding temple inc.'

company_address = '283 franklin st'

company_city = 'boston, ma'

print()

print('\t\t\t*******************************************************************')

print('\t\t\t\t\t\t{}'.format(company_name).title())

print('\t\t\t\t\t\t{}'.format(company_address).title())

print('\t\t\t\t\t\t{}'.format(company_city).title())

print('\t\t\t*******************************************************************')

print("\t\t\t\t\tProduct Name\t Product Price")
print("\t\t\t\t\tBooks\t\t ${}".format(p1_price))
print("\t\t\t\t\tComputer\t ${}".format(p2_price))
print("\t\t\t\t\tMonitor\t\t ${}".format(p3_price))

print('\t\t\t*******************************************************************')
print('\t\t\t\t\tTotal\t\t ${}'.format(total))
print()
print('\t\t\t\t\tThanks for shopping with us today!')
 
print('\t\t\t*******************************************************************')

print()
