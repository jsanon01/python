# This script converts Degree Celsius in Degree Farenheith

number = int(input('What is the Celsius temperature: '))

while number != 0:
    
    f = (9/5 * number) + 32

    print(f'{number} Degree Celcius is {f} Degree Farenheith...')

    print('Enter 0 to exit the loop!')

    number = int(input('What is the Celsius temperature: '))


