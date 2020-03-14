"""
I want to define a class named Person
I want to define 3 attributes named sport, sports, player respectively
I want to create an object named charlot

"""

class Person:
    sport = "the state sports' minister"
    sports = 'the state secretary of sports'
    player = 'the most popular sports in haiti'

charlot = Person()

print('\nCharlot Jacklin Jr is {}'.format(charlot.sports).title())

print()

attys = Person()

print('Max Attys is {}'.format(attys.sport).title())

print()

soccer = Person()

print('soccer is {}'.format(soccer.player))

print()

man = Person()

man.name = 'thomas madiou'.title()

print('{} is one of the famous haitian story-tellers ...'.format(man.name))

print()
