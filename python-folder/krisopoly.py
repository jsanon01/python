# This script prints a while-loop with if-elif statement

questions = print('Enter 1 of the following questions as they appear below: ')
print('where_is_mongolia\t\t','where_is_india')
print('which_wild_cat_lives_in_india\t','name_some_cities_in_massachussets')
print('what_is_a_simple_machine\t', 'name_the_string_instruments')
print('which_month_is_halloween\t', 'which_color_pair_makes the color_vermillon')

day = input('Enter a question: ').lower()

while day != 'q':

    if day == 'which_wild_cat_lives_in_india':
        print('Tiger is a wild cat that cat lives in India?')
    elif day == 'where_is_mongolia':
        print('Mongolia is in East Asia!')
    elif day == 'what_is_a_simple_machine':
        print('A Simple Machine is a Ramp or Inclined Planew!')
    elif day == 'name_the_string_instruments':
        print('They are: violin (the smallest), viola, cello,and doube bass(the biggest)!')
    elif day == 'where_is_india':
        print('India is in South Asia!')
    elif day == 'name_some_cities_in_massachussets':
        print('They are: Boston, Quincy, Cape-Code, Nowrood, Cambridge!')
    elif day == 'which_month_celebrates_halloween_at_the_end':
        print('Halloween always takes place the last day of October!')
    elif day == 'which_color_pair_makes the color_vermillon':
        print('Vermillon is made up of orange and red!')
    elif day == 'sunday':
        print('Happy Sunday .... Sunny Sunday!')
    else:
        print('You have entered a wrong date')

    # print(day)
    print("Engter q to quit")
    day = input('Enter another question: ').lower()

print("You have exited the loop...")
