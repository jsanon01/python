"""
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

def serverless():
    print('fully managed, fault tolerant service')

def ha():
    print('99.99% of SLA availability and 99.999% for Global Tables')

def horizontal():
    print('Auto Scaling and seamless scalability to any scale with push button scaling.')

def no_sql():
    print('flexible schema, suitable for unstructured and unpredictable data')

def streams():
    print('captures a time-ordered sequence of item-level modifications up to 24 hours')

def dax():
    print('fully managed in-memory cache that increases performamce in microseconds.')

def transactions():
    print('strongly or eventually consistent reads supporting ACID transactions')

def backup():
    print('dynamoDB can be used for on-demand backup and restor\npoin-in-time recovery down to the second in last 35 days. ')

def global_tables():
    print('fully managed multi-region, multi-master solution')

def main():
    x = int(input('Enter a number from 0 - 9: '))
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
            print('Invalid number...')
        x = int(input('Enter a number from 0 - 9: '))

    print('You have exited the script!')

main()
