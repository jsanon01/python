# This script prints a printing receipt

# Defining 3 items (variables) in 1 line each

company_name = ''

company_address = ''

company_city  = ''

p1_name = 'Books'

p2_name = 'Computers'

p3_name = 'Monitors'

price = ''

thanks = 'Thanks for shopping with us today!'

print()

print('\t\t\t*******************************************************************')

company_name = 'coding temple inc.'

company_address = '283 franklin st'

company_city = 'boston, mA'


print('\t\t\t\t\t\t{}'.format(company_name).title())

print('\t\t\t\t\t\t{}'.format(company_address).title())

print('\t\t\t\t\t\t{}'.format(company_city).title())

#print("-" * 50)

print('\t\t\t---------------------------------------------------------------------')

p1_price = int(input("\t\t\t\t\tEnter the Books' price: "))

p2_price = int(input("\t\t\t\t\tEnter the Computers' price: "))

p3_price = int(input("\t\t\t\t\tEnter the Monitors' price: "))

total =  p1_price + p2_price + p3_price

#print(total)

print('\t\t\t---------------------------------------------------------------------')

#print()

print("\t\t\t\t\tProduct Name\t Product Price")
print("\t\t\t\t\tBooks\t\t ${}".format(p1_price))
print("\t\t\t\t\tComputer\t ${}".format(p2_price))
print("\t\t\t\t\tMonitor\t\t ${}".format(p3_price))

print('\t\t\t---------------------------------------------------------------------')

print('\t\t\t\t\tTotal\t\t ${}'.format(total))
print()
print('\t\t\t\t\t{}'.format(thanks))
 
print('\t\t\t*******************************************************************')

print()
