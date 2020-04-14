"""
I want to define a function named db()
I want to define another function named partition()
I want to print out both functions

"""

def db():
    print('\nsqs/rdbms\t\t\tdynamodb'.upper())
    print('----------------------------------------------------')
    print('tables\t\t\t\ttables\nrows\t\t\t\titems\ncolumns\t\t\t\tattributes'.title())
    print('indexes\t\t\t\tlocal secondary indexes\nviews\t\t\t\tglobal secondary indexes'.title())
    print("primary keys are:\t\tprimary keys are:".title())
    print("multicolumn and optional\tmin 1 and max 2 attributes, mandatory".title())

db()

print()

def partition():
    print('dynamodb uses synchronous replication'.title())
    print('----------------------------------------------------')
    print('ssd\t<-->\tssd\t<-->\tssd'.upper())
    print('facility 1\tfacility 2\tfacility 3'.title())

partition()

print()
