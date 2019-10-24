# This script prints student info using while-true loop

prompt = 'Enter first name: '

prompts = 'Enter last name: '

#age = 'Enter age: '

while True:
    fname = input(prompt)
    lnames = input(prompts)
 #   age = int(input(age))

    if fname == 'quit':
        break
    elif lnames == 'quit':
        break
    else:
        print(f'Student name is: {fname.title()} {lnames.title()}!')

