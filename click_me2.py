#!/usr/bin/env/python3
from tkinter import *
#from tkinter import ttk
import re

root = Tk()
root.title('New Application')
root.geometry('640x640+0+0')

# --------- these 3 lines are good coding ------------------
#button = ttk.Button(root, text = 'Hello Serverless Architecture').pack() # good coding
#heading = Label(root, text='Welcome to the Serverless World!', font=('Helvetica', 20, 'bold')).pack() # good coding
#label1 = Label(root, text='Enter your name: ', font=('arial', 15, 'bold'), fg='black').pack()

heading = Label(root, text='Welcome to the Serverless World!', font=('arial', 20, 'bold'), fg='steelblue').pack() # good coding

label1 = Label(root, text='Enter your full name: ', font=('arial', 15, 'bold'), fg='black').place(x=10, y=100)

label2 = Label(root, text='Enter phone number: ', font=('arial', 15, 'bold'), fg='black').place(x=10, y=150)

label3 = Label(root, text='Enter E-mail address: ', font=('arial', 15, 'bold'), fg='black').place(x=10, y=200)

name = StringVar()
phone = StringVar()
email = StringVar()

entry_box = Entry(root, textvariable=name, width=25, bg='lightgreen').place(x=170, y=100)
entry_box2 = Entry(root, textvariable=phone, width=25, bg='lightgreen').place(x=170, y=150)
entry_box3 = Entry(root, textvariable=email, width=25, bg='lightgreen').place(x=170, y=200)

def do_it():
    print('Contact Info:\t\t'+ str(name.get()).title())
    print("Phone number is:\t",'(%s) %s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', '0123456789')))
    print('E-mail address is:\t' +str(email.get()))

work = Button(root, text='Click Me', width=23, height=5, bg='lightblue', command=do_it).place(x=160, y=230)

root.mainloop()
