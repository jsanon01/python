"""
I want to create a function called 'general purpose'
I want to create a function called 'compute optimized'
I want to create a function called 'memory optimized'
I want to create a function called 'storage optimized'
I want to create a function called 'advanced computing'
I want to create a function called 'storage features'

I want to define a main function along with a while-statement

"""

print('\nHere are the following EC2 Types, Storage, and Features: ')

print('\n[0] Quit\t\t[1] General Purpose\t[2] Compute Optimized\n[3] Memory Optimized\t[4] Storage Optimized\t[5] Advanced Computing\n[6] Storage Features')

# def EC2():
#    print('\nHere are the following EC2 Types, Storage, and Features: ')

def general_purpose():
    print("\nGeneral Purpose is suitable for worloads that don't use full CPU utilization.\nTheir characteristics are T2, M5, M4 and M3")
    print('\nUse cases: microservices, build servers, code repositories,\ntest and staging environments...')

def compute_optimized():
    print('\nCompute optimized is useful for for workload that is heavy on compute.\nTheir characteristics are: C5, C4, and C3.')
    print('\nUse cases: gaming servers, media transcoding, long-running batch jobs, and HPC...')

def memory_optimized():
    print('\nMemory Optimized is ideal for workload running lots of memory requirements.\nTheir characteristcis are: X1e, X1, R4, and R3.')
    print('\nUse cases: OracleDB in-memory, NoSQL DB like MongoDB, and Cassandra. ')

def storage_optimized():
    print("\nStorage Optimized is ideal for high sequential 'read and write'\naccess to large data sets on local storage.")
    print('\nTheir characteristics are: H1, I3, and D2.')
    print('\nUse cases: data warehouse applications, MapReduce, and Hadoop...')

def advanced_computing():
    print('\nAdvanced computing is for high-processing requirements...\nTheir characteristics are: P3, P2, G3, and F1.')
    print('\nUse cases: genomics, molecular modeling, machine learning algorithms\ncomputationa finance, and computation of fluid dynamics...')

def storage():
    print('\nGeneral Purpose is often used as default volume...EBS volume backed by SSD.\nPIOPS not only maximizes I/O throughput but also cost a little more.\nMaginetic provides the lowest cost...')

def main():

    x = int(input('\nEnter a number from 0 - 6: '))

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
        elif x == 6:
            storage()
        else:
            print('\nYou entered an Invalid number. Try again...')
        x = int(input('\nEnter a number from 0 - 6: '))
    
main()

print('\nExiting the script...!')
#EC2()

print()
