# This script formats phone number

print()

print('Phone Number prints in the following format:\t(XXX)-XXX-XXXX')

while True:

    num = input("\nEnter Phone Number or 'q' to exit: ")

    if num == 'q':

        break

    else:

        print("\nYou entered: ("+num[:3]+")"+num[3:6]+"-"+num[6:])

print('\nYou have exited the script')        

print()
