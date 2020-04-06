info = ''

berger = ''

class shepherd:
    def __init__(self, mouton, brebis):
        self.mouton = mouton
        self.brebis = brebis

    def info(self):
        p = self.brebis
        z = self.mouton
        print('\nJe suis le {} {}'.format(z, p))
        print('\nJe connais mes brebis et mes brebis me connaissent...')

radio = shepherd('bon'.title(), 'berger'.upper())

radio.info()

print(info)
