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

# setting up the heading in light blue
heading = Label(root, text='Welcome to the Serverless World!', font=('arial', 20, 'bold'), fg='steelblue').pack() # good coding

# setting up 3 labels for 1) full name 2) phone 3) email
label1 = Label(root, text='Enter your full name: ', font=('arial', 15, 'bold'), fg='black').place(x=10, y=100)

label2 = Label(root, text='Enter phone number: ', font=('arial', 15, 'bold'), fg='black').place(x=10, y=150)

label3 = Label(root, text='Enter E-mail address: ', font=('arial', 15, 'bold'), fg='black').place(x=10, y=200)

# declaration of 3 string variables
name = StringVar()
phone = StringVar()
email = StringVar()

# setting up 3 entries for the 3 labels
entry_box = Entry(root, textvariable=name, width=25, bg='lightgreen').place(x=170, y=100)
entry_box2 = Entry(root, textvariable=phone, width=25, bg='lightgreen').place(x=170, y=150)
entry_box3 = Entry(root, textvariable=email, width=25, bg='lightgreen').place(x=170, y=200)

# function that will print out entries in backend (in terminal)
def do_it():
    print('Hello '+ str(name.get()).title())
    print("Phone number is: ",'(%s) %s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', '0123456789')))
    print('your e-mail address is: '.title())

# setting up widget to exit program
work = Button(root, text='Send', width=23, height=5, bg='lightblue', command=do_it).place(x=160, y=230)

button_quit = Button(root, text='Exit Program', command=root.quit).place(x=210, y=315)

#button_quit.pack()

# running the program
root.mainloop()
