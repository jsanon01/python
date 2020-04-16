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

def descriptive():
    print('\nDescriptive Analytic...is based on REPORTS & ALERTS.\n\nWhat happened?')
   
def diagnostic():
    print('\nDiagnostic Analytic...is based on QUERIES & DATA MINING.\n\nWhy did it happen?')

def predictive():
    print('\nPredictive Analytic...is based on FORECAST & SIMULATIONS.\n\nWhat is likely to happen?')

def prescriptive():
    print('\nPrescriptive Analytic...is based on PLANNING & OPTIMIZATION.\n\nWhat can we do to make it happen?')

def basic():
    print('\n- mean\t- median\t- variance\n- coun\t- top-n\t- distinct')

def generalized():
    print('\n- distnaces\t- kernels\t- similarity\n- nearest\t- neighbor\t- clustering\t- cluster svm')

def linear():
    print('\nlinear algebra\t- linear regression\t- pca')

def graph():
    print('\ngraph search\t- betweenness\t- centrality\n- commute distance\t- shortest path\tmin spanning tree')

def optimization():
    print('\nminimization\t- maximization\t- linear\t- quadratic programming\t- gradient descent')

def integration():
    print('\n- bayesian inference\t- expectations\t- markov chain\n- monte carlo')

def alignment():
    print('hidden markov model\t- matching data sets(texts, images, sequences)')

def main():
    x = int(input('\nEnter a number: '))
    while x:
        if x == 1:
            descriptive()
        elif x == 2:
            diagnostic()
        elif x == 3:
            predictive()
        elif x == 4:
            prescriptive()
        else:
            print('Invalid number...')
        x = int(input('\nEnter a number: '))

    print('\nYou have exited the script...')

main()

print()
