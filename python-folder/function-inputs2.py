# This script prints out  inputs from a function

def fonction(words):

    fname = input('Enter first name: ').title()

    lname = input('Enter last name: ').title()

    address = input('Enter Address: ').title()

    zip_code = input('Enter Zip Code: ').title()

    email = input('Enter Email address: ').lower()

    num = input('Enter Phone number: ')

    print('----------------- Here is the output ----------------')
    
    print('First Name: {}\nLast Name: {}\nAddress: {}\nZip Code: {}\nEmail Address: {}\nPhone Number: {}'.format(fname, lname, address, zip_code, email, ("("+num[:3]+")"+ num[3:6]+ "-"+ num[6:])))


words = ''

fonction(words)
num = ''

#def phoneNumbers():
#    print("("+num[:3]+")"+ num[3:6]+ "-"+ num[6:])


#phoneNumbers()
