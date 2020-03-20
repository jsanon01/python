"""
I want to define a function named dynamodb
I want to define a function named ad_tech
I want to define a function named gaming
I want to define a function named retail
I want to define a function named banking
I want to define a function named media
I want to define a function named os_and_internet

I want to define a main function with a while statement:
- to quit when x = 0
- to call retail when x = 1
- to call banking when x = 2
- to call ad_tech when x = 3
- to call media when x = 4
- to call os_and_internet when x = 5
- to call gaming when x = 6


"""

def dynamodb():
   print("\nhere are the most common use cases for dynamo db:\n".upper())

def ad_tech():
    print("\nad tech:\n- user events and clickstreams\t- impressions data store.\n- metadata store for assets\t- popular-item caches\n- user profile stores in rtb and targeting.\n".title())

def gaming():
    print("\ngaming:\n- game states\t- player data stores\n- leaderboards\t- player sessionnhistory data stores\n".title())

def retail():
    print("\nretail:\n- shopping carts\t- workflow engines\n- inventory tracking\t- customer profile and accounts\n".title())

def banking():
    print("\nbanking and finance:\n- user transactions\t- fraud detection\n- event-driven transaction processing\t- mainframe offloading\n- change data capture\n".title())

def media():
    print("\nmedia and entertainment:\n- media metadata stores\t- user data stores\n- digital rights management data stores\n".title())

def os_and_internet():
    print("\nfoftware and internet:\n- ride-tracking data stores\t- metadata caches\n- user content metadata stores\t- relationship graph data stores\n- user, vehicle and driver data stores\n".title())

dynamodb()
print('[0] Quit\t[1] Retail\t[2] Banking\t[3] Ad Tech\n[4] Media\t[5] OS & Cloud\t[6] Gaming')

def main():
    x = int(input('\nEnter a number from 0 - 6: '))
    while x:
        if x == 1:
            retail()
        elif x == 2:
            banking()          
        elif x == 3:
            ad_tech()
        elif x == 4:
            media()
        elif x == 5:
            os_and_internet()
        elif x == 6:
            gaming()
        else:
            print('Invalid numbner..!')
        x = int(input('Enter a number from 0 - 6: '))

    print('Exiting the script...!')

main()
print()

"""
def webapp():
    print(severless web apps)

def mobile():
    print(mobile backends)

def microservices():
    print()
"""
