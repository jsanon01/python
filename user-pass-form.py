from tkinter import *
from functools import partial

def validateLogin(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
    return

# setting up window-frame
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')

# setting up username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

# setting up password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

# setting up login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

# exiting and running the program
tkWindow.mainloop()
