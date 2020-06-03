#!/usr/bin/env/python3
from tkinter import *
#from tkinter import ttk

root = Tk()
root.title('New Application')
root.geometry('640x640+0+0')
# --------- these 3 lines are good coding ------------------
#button = ttk.Button(root, text = 'Hello Serverless Architecture').pack() # good coding
#heading = Label(root, text='Welcome to the Serverless World!', font=('Helvetica', 20, 'bold')).pack() # good coding
#label1 = Label(root, text='Enter your name: ', font=('arial', 15, 'bold'), fg='black').pack()

heading = Label(root, text='Welcome to the Serverless World!', font=('arial', 20, 'bold'), fg='steelblue').pack() # good coding

label1 = Label(root, text='Enter your name: ', font=('arial', 15, 'bold'), fg='black').place(x=10, y=100)

name = StringVar()

entry_box = Entry(root, textvariable=name, width=25, bg='lightgreen').place(x=160, y=100)

def do_it():
    print('Hello ' + str(name.get()).title())


work = Button(root, text='Click Me', width=23, height=5, bg='lightblue', command=do_it).place(x=160, y=140)

root.mainloop()