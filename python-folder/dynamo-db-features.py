"""
I want to print out a menu for the functions mentioned below...
I want to define a function named serverless
I want to define a function named highly_available
I want to define a function named horizontal_scaling
I want to define a function named no_sql
I want to define a function named streams
I want to define a function named dax
I want to define a function named transactions
I want to define a function named backup
I want to define a function named global_tables

I want to define a main function with a while statement:
- to quit when x = 0
- to call serverless when x = 1
- to call highly_available when x = 2
- to call horizontal when x = 3
- to call no_sql when x = 4
- to call streams when x = 5
- to call dax when x = 6
- to call transactions when x = 7
- to call backup when x = 8
- to call global_tables when x = 9
		
"""
print('\n[0] Quit\t[1] Serverless\t\t[2] Availability\t[3] Scaling')
print('[4] No SQL\t[5] DynamDB Streams\t[6] DAX\t\t\t[7] Transactions\n[8] Backup\t[9] Global Tables')

def serverless():
    print('\nDynamoDB is fully managed, fault tolerant service.')

def ha():
    print('\nDynamoDB is 99.99% of SLA availability and 99.999% for Global Tables.')

def horizontal():
    print('\nDynsmoDB uses Auto Scaling and seamless scalability to any scale with push button scaling.')

def no_sql():
    print('\nDynamoDB is a flexible schema, suitable for unstructured and unpredictable data.')

def streams():
    print('\nDynamoDB captures a time-ordered sequence of item-level modifications up to 24 hours.')

def dax():
    print('\nDynamoDB is a fully managed in-memory cache that increases performamce in microseconds.')

def transactions():
    print('\nDynamDB uses strongly or eventually consistent reads supporting ACID transactions.')

def backup():
    print('\nDynamoDB can be used for on-demand backup and restor\npoin-in-time recovery down to the second in last 35 days. ')

def global_tables():
    print('\nDynamoDB is a fully managed multi-region, multi-master solution.')

def main():
    x = int(input('\nEnter a number from 0 - 9: '))
    while x:
        if x == 1:
            serverless()
        elif x == 2:
            ha()
        elif x == 3:
            horizontal()
        elif x == 4:
            no_sql()
        elif x == 5:
            streams()
        elif x == 6:
            dax()
        elif x == 7:
            transactions()
        elif x == 8:
            backup()
        elif x == 9:
            global_tables()
        else:
            print('\nInvalid number...')
        x = int(input('\nEnter a number from 0 - 9: '))

    print('\nYou have exited the script!')

main()

print()
