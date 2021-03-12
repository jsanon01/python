"""
polymorphism with class method

"""


class India:
    def capital(self):
        print('\nnew delhi is the capital of india')

    def language(self):
        print('\nhindi is the most widely spoken language.')

    def type(self):
        print('\nindia is a developing country.')


class USA:
    def capital(self):
        print('\nwashington is the capital.')

    def language(self):
        print('\nenglish is the spoken language.')

    def type(self):
        print('\nusa is a developed country.')

patel = India()
kiki = USA()

for country in (kiki, patel):
    country.capital()
    country.language()
    country.type()

print()
