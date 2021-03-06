from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):

        self.label = ttk.Label(master, text='greetings!'.upper())
        self.label.grid(row = 0, column = 0, columnspan = 2 )

        ttk.Button(master, text = 'India', command= self.india_hello).grid(row=3, column=1)

        ttk.Button(master, text = 'brasil'.title(), command = self.texas_hello).grid(row=2, column=1)

        ttk.Button(master, text = 'Hawaii', command = self.hawaii_hello).grid(row=3, column=0)

        ttk.Button(master, text = 'Haiti', command= self.haiti_hello).grid(row=1, column=0)

        ttk.Button(master, text = 'Canada', command= self.canada_hello).grid(row=2, column=0)

        ttk.Button(master, text = 'U.S.A.', command= self.america_hello).grid(row=1, column=1)


        button_quit = Button(master, text = 'Exit Program', command=master.quit).grid(row=4, column=0)

    def haiti_hello(self):
        self.label.config( text = 'Sak Pase Haiti!')

    def america_hello(self):
        self.label.config( text = 'Good Morning America!')

    def canada_hello(self):
        self.label.config( text= 'Bonjour Canada!')

    def texas_hello(self):
        self.label.config( text= "bom dia Brasil!")

    def hawaii_hello(self):
        self.label.config( text= 'Aloha Hawaii!')

    def india_hello(self):
        self.label.config( text = 'Namaste India!')

def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if __name__ == "__main__": main()
