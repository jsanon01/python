"""
I want to create a class named Argentina
I want to create 4 functions inside the class named Argentina
- capital - language -currency - independence - labor_day

I want to create a class named Jamaica
I want to create 4 functions inside the class named Argentina
- capital - language -currency - independence - labor_day

I want to instantiate bot Argentina and Jamaica
I want to print out classes and functions using for-loop
"""

class Argentina:
    def capital(self):
        print('\nthe capital of argentina is Buenos-Aires'.title())

    def language(self):
        print('\nspanish is the spoken language in argentina.'.title())

    def currency(self):
        print('\nargentina currency is peso.'.title())

    def independence(self):
        print("\nargentina independence day is on july 9th.".title())

    def labor(self):
        print('\nargentina labor day is celebrated may 1st.'.title())
#print('----------------------------------------------------------------------')
class Jamaica:
    def capital(self):
        print('\nthe capital of jamaica is kingston.'.title())

    def language(self):
        print('\nenglish is the spoken language in jamaica.'.title())

    def currency(self):
        print('\njamaican dollar is their currency.'.title())

    def independence(self):
        print("\njamaica independence day is on august 6th.".title())

    def labor(self):
        print('\njamaican labor day is celebrated may 1st.'.title())

messi = Argentina()

reggae_boys = Jamaica()

for country in (messi, reggae_boys):
    country.capital()
    country.language()
    country.currency()
    country.independence()
    country.labor()

print()
