# This script prints a while-loop with if-elif statement 

def week(school):
        switcher = {
            1:'Helps with Weight Loss',
            2:'Helps with Stomach Ache & Constipation Relief',
            3:'Heals Liver injuries',
	    4:'Boosts Heart Health',
            5:'Controls Diabetes and Hperglycemia',
            6:'Prevents Malaria and Microbial Diseases',
            7:'Helps with Exfoliation and Skin brightener',
	    8:'Improves Circulation and Nerve Functions',
            9:'Improves Your Immune System',
            10:'Helps with Dental Health',
            11:'Can Promote Good Sexual Health',
            12:'May Boost Yout Taste Buds',
            13:'Helps the Brain Heal',
            14:'Promotes Good Sleeping Patterns',
            15:'Helps the Body Process Foods',
            16:'Boosts Your Vision',
   
        }
        return switcher.get(school,"Invalid Grade")

year = " "

while year != 'q':
    if year.isdigit(): # '1'.digit() 'w'.isdigzit() 'karlo'.isdigit()
        result = week(int(year))
        print(result)
    year = input('Enter a number from 1 - 16 or q to quit: ')
