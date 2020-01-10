"""
I want a function named 'compute'
I want a function named 'storage'
I want a function named 'data_stores'
I want a function named 'api_proxy'
I want a function named 'api_integration'
I want a function named 'analytics'
I want a function named 'dev_tool'

I want to print out a menu to display 'main loop function'
I want a while statement inside the  main function
"""

def compute():
    print('Compute:\n- Lambda lets you run code without provisioning servers.\n- Lamda Edges manages CloudFront.\n- Fargate is a built-purpose containers.')

def storage():
    print('Storage:\n- S3 provides secure web interface from any web around the world.\n- EFS provides simple, and elastic file storage.')

def data_stores():
    print('Data Stores:\n- Dynamo DB is no sql.')

def api_proxy():
    print('API Proxy:\nAPI Gateway...')
    
def api_integration():
        print('Application Integration:\nAPI Integration...')

def analytics():
        print('Analytics:\nAnalytics.....')

def dev_tool():
        print('Developer Tools:\nDev tool....')




print("\nThis script prints out a Menu to display 'Main Loop function.'")


def main():
    print("\nHere are the following AWS 'serverless' services:\n[0] Quit\t[1] Compute\t\t[2] Storage\t[3] Data Stores\n[4] API Proxy\t[5] API Integration\t[6] Analytics\t[7] Dev Tools\n[8] Reference ")
    print()
    compute()
    print()
    storage()
    print()
    data_stores()
    print()
    api_proxy()
    print()
    api_integration()
    print()
    analytics()
    print()
    dev_tool()
    print()

main()
