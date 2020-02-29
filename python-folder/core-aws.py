"""
I want to define 2 for loops
- one for core services
- another one for well-architected framework

"""

list_1 = {
	'vpc': 'virtual private cloud provides the networking foundation for aws services.',
	'ec2':'elastic compute cloud provides computing resources.',
	'iam': 'identity access management provides fine-grained access contol.',
	's3': 'simple storage service offers several storage solutions.',
	'rte 53':'route 53 deals with dns, and routing.'
	}

print('\nHere are the 2 main  parts of Solution Architect Associates')

print('\n1- The Core Services:')

for k, v in list_1.items():
    print('\n- {} means {}'.format(k,v).upper())

print('\n-----------------------------------------------------------------')

list_2 = { 
	'reliability': 'how the solution can recover from various failures.',
	'performance efficiency':'the need for speed.',
	'security': 'the business secured top priority at the heart of everything.',
	'cost optimization':'eliminates unneeded cost or suboptimal resources.',
	'operational excellence':'how the system is able to support the business.',

	}

print('\n2- The Well-Architected Framework:')

for k, v in list_2.items():
    print('\n- {} means {}'.format(k,v).upper())

print()
