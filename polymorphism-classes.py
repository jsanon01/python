"""


"""


class Fed:
    def fed(self):
        print('\nthe president rules the federal government.'.title())

    def state(self):
        print('\na state is ruled by a governor.'.title())

    def county(self):
        print('\na county is governed by representatives.'.title())

    def city(self):
        print('\na city is ruled by a mayor'.title())

    def town(self):
        print('\na town has a board of elected selectmen'.title())

class Haiti:
    def fed(self):
        print('\nrepublic haiti is ruled by a president and prime minister.'.title())

    def state(self):
        print("\nhaiti is divided in 10 departments.".title())

    def county(self):
        print('\na delegated official rules the department.'.title())

    def city(self):
        print('\nmayor rules the city with 2 othe members.'.title())

    def town(self):
        print('\nasec/casec officials runs communal sections'.title())

fed = Fed()
haiti = Haiti()

for country in (fed, haiti):
    country.fed()
    country.state()
    country.county()
    country.city()
    country.town()

print()
