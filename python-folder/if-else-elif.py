# This script is about control statement
# for + if-elif-else statement

companies = [ 'verizon', 'comcast', 'rcn', 'bell', 'rogers']

for company in companies:
    if company == 'rcn':
        print(company.upper())
#    elif company == 'bell':
#        print(company.title())
    else:
        print(len(companies))
