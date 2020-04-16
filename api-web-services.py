"""
I want to define a function named type()
I want to define a function named soap()
I want to define a function named rest()
I want to define a function named client()
I want to define a function named server()
I want to define a main function

https://www.youtube.com/watch?v=B3-BEY7Mv_8
https://www.upwork.com/search/profiles/?nbs=1&q=cloud&profile=~0107cd83ec37495694

"""
print()

def type():
    print('\n2 types of api web services:\n- soap which is built on different cross-platforms\n- restful which works with all media components, files, or objects.'.upper())


def soap():
    print('SOAP => simple object access protocol'.title())
    print('\nmedium: http (post)\t\t\tformat: xml'.upper())

def rest():
    print('\nREST => representational state transfer'.title())
    print('\nmedium: http (post, get, put, delete)\tformat: xml/json/text'.upper())

def client():
    print('\nCLIENT => is service consumer | Always REQUEST')
    print('\nmedium: http/internet\t\t\tformat: xml/json'.upper())

def server():
    print('\nSERVER => is service provider | Always RESPOND')
    print('\nmedium: http/internet\t\t\tformat: xml/json'.upper())


def main():
    type()
    print()
    soap()
    rest()
    client()
    server()

main()
print()
