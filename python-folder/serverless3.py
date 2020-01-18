"""
I want to import website for Reference
I want a function named 'compute'
I want a function named 'storage'
I want a function named 'data_stores'
I want a function named 'api_proxy'
I want a function named 'api_integration'
I want a function named 'analytics'
I want a function named 'dev_tool'
I want a function named 'orchestration'

I want to print out a menu to display 'main loop function'
I want a while statement inside the  main function calling sub-functions

"""

import webbrowser


def compute():
    print('Compute:\n- Lambda lets you run code without provisioning servers.\n- Lamda Edges manages CloudFront.\n- Fargate is a built-purpose containers.')

def storage():
    print('Storage:\n- S3 provides secure web interface from any web around the world.\n- EFS provides simple, and elastic file storage.')

def data_stores():
    print('Data Stores:\n- DynamoDB is a fast and flexible No SQL DB.\n- Aurora Serverless is an auto-scaling configuration for Aurora/MySQL.\n- Amazon RDS Proxy is a H.A. DB managing 1000 of connections to relational DBs.')

def api_proxy():
    print('API Proxy:\nAPI Gateway is a fully managed service to create, maintain, publish, monitor, and secure APIs at any scale....')
    
def api_integration():
        print('Application Integration:\n- Amazon SNS is a fully managed pub/sub messaging service designing to decouple and scale microservices.\n- Amazon SQS is a fully managed message queuing service designing to decouple and scale microservices.\n- AWS AppSync simplifies application development by creating data from one or more data sources.\n- Amazon EventBridge is a serverless event bus service designing to access application from a variety of sources to your AWS environment.\n...')

def analytics():
        print('Analytics:\n- Amazon Kinesis is a platform for streaming data on AWS.\n- Amazon Athena is an interactice query analyzing data into S3 using standard SQL.')

def dev_tool():
        print('Developer Tools:\n- AWS provides tools and services that aid developers in the serverless application development process.')

def orchestration():
    print('AWS Step Functions:\n- AWS Step Functions coordinates the components of distributed applications using visual workflows.')




print("\nThis script prints out a Menu to display 'Main Loop function.'")


def main():

        print("\nHere are the following AWS 'serverless' services:\n[0] Quit\t\t[1] Compute\t\t[2] Storage\t[3] Data Stores\n[4] API Proxy\t\t[5] API Integration\t[6] Analytics\t[7] Dev Tools\n[8] Orchestration\t[9] Website\n ")

        while 1:
            
            aws = input('Enter a number from 0 - 9 (bis): ')
            
            if not aws.isdigit() or int(aws) == 0:
                print('Exiting the script...!')
                break
            else:
                aws = int(aws)

            if aws == 1:
                compute()

            elif aws == 2:
                storage()

            elif aws == 3:
                data_stores()

            elif aws == 4:
                api_proxy()

            elif aws == 5:
                api_integration()

            elif aws == 6:
                analytics()

            elif aws == 7:
                dev_tool()

            elif aws == 8:
                orchestration()

            elif aws == 9:
                webbrowser.open('https://aws.amazon.com/serverless/')

            else:
               print('Invalid number.')

main()


