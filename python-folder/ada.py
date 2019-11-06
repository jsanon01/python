# This scripts greets Ada in a function

person = 'ada'

def greet(person):
    print("Hello",  person.title())
    print(person.title(),' what are you up to?')
    print("Let's have some fun", person.title())

print('--- Original Function ---')

greet(person.title())


print('--- Copy-Cat Function ---')

greet('emily')

print('--- Copy-Cat Function ---')

greet('jenny')
