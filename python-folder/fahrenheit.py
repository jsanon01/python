# This script converts Degree Fahrenheit to Celsius

number =int(input('What is the Fahrenheit temperature: '))

while number != 0:

    c = (number - 32) * 5/9
    
    print(f'{number} Degree Fahrenheit is {c} Degree Celsius...')
    
    print('Enter q to exit the program!')

    number =int(input('What is the Fahrenheit temperature: '))

