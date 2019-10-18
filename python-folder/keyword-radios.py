# Script related to Haitian radios
# with keyyword as function

def keyword(rad_1, rad_2, rad_3):
    print()
    print('\n'+ 'Here are some Haitian radio stations:\n' +'\n'+  rad_1 +  '\n' + rad_2 + '\n' + rad_3)

keyword(rad_1 = 'Radio Metropole --> 100.1 FM Stereo\n', rad_2 = 'Radio Kiskeya --> 89.1 FM Mono\n', rad_3 = 'Radio Vision 2000 --> 99.3 FM Stero')

print('-------------------------------')
with open('haitian-tvs.txt') as file_object:
    content = file_object.read()
    print(content)
