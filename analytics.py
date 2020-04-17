"""
I want to define a function named descriptive()
I want to define a function named diagnostic()
I want to define a function named predictive()
I want to define a function named prescriptive()

I want to define a function named basic()
I want to define a function named generalized()
I want to define a function named linear()
I want to define a function named graph()
I want to define a function named optimization()
I want to define a function named integration()
I want to define a function named alignment()

I want to define a main function including a while loop
- to quit when x = 0
- to call descriptive when x = 1
- to call diagnostics when x = 2
- to call predictive when x = 3
- to call prescriptive when x = 4
- to call descriptive when x = 1
- to call descriptive when x = 1
- to call descriptive when x = 1
- to call descriptive when x = 1
- to call descriptive when x = 1


p 23 1.1

"""

print("\ntypes of analytics".title())
print('\n[0] Quit [1] descriptive [2] diagnostic\t[3] predictive\t[4] prescriptive'.title())
print("\n7 computational tasks for analytics".title())
#print('\n[11] statistics [2] n-body problem [3] linear computations\t[4] graph computations\n[5] optimization [6] integration\t[7] alignment problems'.title())
print('\n[11] descriptive [21] diagnostic\t[31] predictive\t[41] prescriptive'.title())


def descriptive():
    print("\nDescriptive Analytic...is based on REPORTS & ALERTS.\n\nDescriptive Analytic deals with 'What happened?'")
   
def diagnostic():
    print("\nDiagnostic Analytic...is based on QUERIES & DATA MINING.\n\nDiagnostic Analytic deals with 'Why did it happen?'")

def predictive():
    print("\nPredictive Analytic...is based on FORECAST & SIMULATIONS.\n\nPredictive Analytic deals with 'What is likely to happen?'")

def prescriptive():
    print("\nPrescriptive Analytic...is based on PLANNING & OPTIMIZATION.\n\nPrescriptive Analytic deals with nWhat can we do to make it happen?'")

def basic():
    print('\n-------- basic statistics --------\n- mean\t- median\t- variance\n- coun\t- top-n\t\t- distinct'.title())

def generalized():
    print('\n-------- n-body problem --------\n- distnaces\t- kernels\t- similarity\n- nearest\t- neighbor\t- clustering\t- cluster svm'.title())

def linear():
    print('\n-------- linear algebraic computations --------\nlinear algebraic computations\n- linear algebra\t- linear regression\t- pca'.title())

def graph():
    print('\n-------- graph computations --------\n- graph search\t- betweenness\t- centrality\n- commute distance\t- shortest path\tmin spanning tree'.title())

def optimization():
    print('\n-------- optimization --------\n- minimization\t- maximization\t- linear\t- quadratic programming\t- gradient descent'.title())

def integration():
    print('\n-------- integration --------\n- bayesian inference\t- expectations\t- markov chain\n- monte carlo'.title())

def alignment():
    print('\n-------- alignment problems --------\n- hidden markov model\t- matching data sets(texts, images, sequences)'.title())

def main():
    x = int(input('\nEnter a number: '))
    while x:
        if x == 1:
            descriptive()
        elif x == 11:
            basic()
            linear()
        elif x == 2:
            diagnostic()
        elif x == 21:
            generalized()
            linear()
            graph()
        elif x == 3:
            predictive()
        elif x == 31:
            generalized()
            linear()
            graph()
            integration()
            alignment()
        elif x == 4:
            prescriptive()
        elif x == 41:
            generalized()
            graph()
            optimization()
            integration()
            alignment()
        else:
            print('Invalid number...')
        x = int(input('\nEnter a number: '))

    print('\nYou have exited the script...')

main()

print()
