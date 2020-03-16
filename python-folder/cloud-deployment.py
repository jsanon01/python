"""
I want to define a function named cloud
I want to define a function named cost
I want to define a function named operation
I want to define a function named elasticity

I want to define a main function with a while-statement
- to quit when x = 0
- to call app-deployment when x = 1, lambda when x = 2, api when x = 3
- to call kinesis when x = 4, kds when x = 5, kda when x = 6, reference when x = 7
- to call cloudfront when x = 8, waf when x = 9, sqs when x = 10, steps when x = 11
- to call sns when x = 12, swf when x = 13, ops when x = 14, emr when x = 15
- to call cloudformation when x = 16, cloudwatch when x = 17, trusted when x = 18, organizations when x = 19

"""

def cloud():
    print("\n'to build effective solutions, architects need an in-depth knowledge of\nthe application and deployment services on AWS.'\n\t\t\t\t\t\tTom Carpenter".upper())

def cost():
    print('\nA. designing cost-optimized compute:\n[1] application-deployment services\t[2] Lambda\t[3] API Gateway\n[4] Kinesis\t[5] Kinesis Data Streams & Firehose\t[6] Kinesis Data Analytics\n[7] Reference Architectures '.title())

def operation():
    print('\nB. designing for operational excellence:\n[8] cloudfront\t[9] Web Application Firewall\t[10] Simple Queue Service\n[11] Step Functions\t[12] Simple Notification Service [13] Simple Workflow'.title())

def elasticity():
    print('\nC. designing for elasticity and scalability:\n[14] opsworks\t[15] elastic map reduce\t\t[16] cloudformation\n[17] cloudwatch\t[18] Trusted advisor\t\t[19] organisations'.title())

def app():
    print("\napplication deployment is a 'cloud conceptual perspective of the services':\n'how are they used?'\t'why should i use one of them?' ")

def lambda_functions():
    print('\nlambda is not only a serverless computing service but also scales automatically up to 1,000 requests.')

def api():
    print('\napi gateway is not only a standard way to accomplish automatic tasks\nbut also is API Management in the cloud.')

def kinesis():
    print('\nkinesis data streams helps to manage incoming data streams, do analysis of it, gets it where you need to go.')

def kinesis_firehose():
    print("\nKinesis Data Firehose is the easiest way to reliably load streaming data into data lakes\ndata stores, and analytics tools.")

def kda():
    print('\nkinesis data analytics a great powerful tool service to narrow down your search based on standard SQL Queries.')

def reference():
    print('\nrefernce architectures is a well-architected framework for specific solution complying with a set of requirements.')

def cloudfront():
    print('\ncloudfront is a fast, highly secure and programmable service for static and dynamic contents. ')

def waf():
    print("\nweb application firewall (WAF) uses extra level of security for 'public-facing' and 'web applications.'")

def sqs():
    print('\nSimple Queue Service is implemented to allow decoupling applications.\nMessages are queued and processed asynchronously meaning out of order.')

def step():
    print('\nAWS recommends Step Functions practice as replacement of Simple WorkFlow ')

def sns():
    print("\nSimple Notification Service is like 'messaging or paging in the cloud.'\nSNS uses 'pub-sub model' meaning publish-subscriber model ")

def swf():
    print('\nSimple WokFlow not only is a decoupled application service nut also\ndefines the sequence of events required to achieve a workflow.')

def ops():
    print('\nOpsWorks is the configuration management solution in AWS')

def emr():
    print("\nElastic Map Reduce uses 'Master Nodes for distributors,''Core Nodes for process and storage,''Task Nodes for the work'")

def cloudformation():
    print('\nCloudFormation is the key for deployment of multiple instances to form a complete solution.')

def cloudwatch():
    print('\nCloudWatch monitors the cloud and on-premises, logs data out to build dashboards,\nsends SNS and SMS alarms for launching or restarting instances.')

def trusted():
    print("\ntrusted advisor is your trusting and trusty friend in the cloud.\n'improving security'\t'improving performance'\t'reducing cost'\n'improving fault tolerance'")

def organizations():
    print('\nAWS Organizations is a collection of AWS accounts at No additional charge for use.')

def main():
    cloud()
    print('------------------------------------------------------------------')
    cost()
    operation()
    elasticity()

    x = int(input('\nEnter a number from 0 - 20: '))
    while x:
        if x == 1:
            app()
        elif x == 2:
            lambda_functions()
        elif x == 3:
            api()
        elif x == 4:
            kinesis()
        elif x == 5:
            kinesis_firehose()
        elif x == 6:
            kda()
        elif x == 7:
            reference()
        elif x == 8:
            cloudfront()
        elif x == 9:
            waf()
        elif x == 10:
            sqs()
        elif x == 11:
            step()
        elif x == 12:
            sns()
        elif x == 13:
            swf()
        elif x == 14:
            ops()
        elif x == 15:
            emr()
        elif x == 16:
            cloudformation()
        elif x == 17:
            cloudwatch()
        elif x == 18:
            trusted()
        elif x == 19:
            organizations()
        else:
            print('\nInvalid number!')
        x = int(input('\nEnter a number from 0 - 20: '))

    print('\nYou have exited the script...!')

main()

print()
