from tkinter import *
from tkinter import messagebox
import sqlite3
import runpy

#for signin and signup initializing database
logindata = sqlite3.connect('users.db')
cursor=logindata.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS users(
    username text PRIMARYKEY,
    password text NOT NULL
    )
    '''
)
logindata.commit()

login=Tk()
login.title('Library Management System Login')
login.attributes("-fullscreen",True)

#to show and hide password
def showpassword():
    a=checkbutton.get()
    if a==1:
        passwordentry.config(show="")
    else:
        passwordentry.config(show="*")

#to check username and passsword
def signin():
    username = usernameentry.get()
    password = passwordentry.get()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if cursor.fetchone():
        login.destroy()
        runpy.run_path('dashboard.py')
      

    else:
        usernameentry.delete(0,END)
        passwordentry.delete(0,END)
        messagebox.showerror('Warning', 'Incorrect password or username')

#to make new account
def signup():
    username = usernameentry.get()
    password = passwordentry.get()
    if username and password:
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        if cursor.fetchone():
            messagebox.showerror('Error', 'Username already exists')
        else:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            logindata.commit()
            usernameentry.delete(0,END)
            passwordentry.delete(0,END)
            messagebox.showinfo('Success', 'Account created successfully!')
    else:
        messagebox.showerror('Error', 'Please enter both username and password')


username = Label(login, text='Username:').place(x=40, y=50)
password = Label(login, text='Password:').place(x=40, y=100)

usernameentry = Entry(login)
usernameentry.place(x=120, y=50)


passwordentry = Entry(login, show='*')
passwordentry.place(x=120, y=100)

checkbutton = IntVar()
showpasswordbutton = Checkbutton(login, text='Show', variable=checkbutton, command=showpassword)
showpasswordbutton.place(x=75, y=200)

b = Button(login, text='Login', command=signin)
b.place(x=85, y=300)

s = Button(login, text='Signup', command=signup)
s.place(x=85, y=350)

def exit_fullscreen(event):
    login.attributes("-fullscreen",False)

login.bind('<Escape>',exit_fullscreen)
login.mainloop()
logindata.close()