"""
I want to define a class named Javascript
I want to define a method named front-end
I want to define a method named back-end

"""
class Javascript:

    def frontend(self):
        print('\njavascript is interactive on the front-end side (users)'.upper())

    def backend(self):
        print('\njavascript is static on the back-end side (servers).'.upper())


js = Javascript()

js.frontend()
js.backend()
print()
