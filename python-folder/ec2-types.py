"""
I want to define a function called EC2
I want to create a function called 'general purpose'
I want to create a function called 'compute optimized'
I want to create a function called 'memory optimized'
I want to create a function called 'storage optimized'
I want to create a function called 'advanced computing'

I want to define a main function along with a while-statement

"""

def EC2():
    print('EC2')

def general_purpose():
    print("General Purpose is suitable for worloads that don't use full CPU utilization.\nTheir characteristics are T2, M5, M4 and M3")
    print('Use cases: microservices, build servers, code repositories,\ntest and staging environments...')
def compute_optimized():
    print('Compute optimized is useful for for workload that is heavy on compute.\nTheir characteristics are: C5, C4, and C3.')
    print('Use cases: gaming servers, media transcoding, long-running batch jobs, and HPC...')
def memory_optimized():
    print('Memory Optimized is ideal for workload running lots of memory requirements.\nTheir characteristcis are: X1e, X1, R4, and R3.')
    print('Use cases: OracleDB in-memory, NoSQL DB like MongoDB, and Cassandra. ')

def storage_optimized():
    print("Storage Optimized is ideal for high sequential 'read and write'\naccess to large data sets on local storage.")
    print('Their characteristics are: H1, I3, and D2.')
    print('Use cases: data warehouse applications, MapReduce, and Hadoop...')

def advanced_computing():
    print('Advanced computing is for high-processing requirements...\nTheir characteristics are: P3, P2, G3, and F1.')
    print('Use cases: genomics, molecular modeling, machine learning algorithms\ncomputationa finance, and computation of fluid dynamics...')



def main():
    x = int(input('enter a number: '))
    while x:
        if x == 1:
            general_purpose()
        elif x == 2:
            compute_optimized()
        elif x == 3:
            memory_optimized()
        elif x == 4:
            storage_optimized()
        elif x == 5:
            advanced_computing()
        else:
            print('Invalid number')
        x = int(input('enter a number: '))
    

EC2()

main()
