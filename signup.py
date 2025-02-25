from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk


signupwindow=Tk()
signupwindow.title('Sign UP')
signupwindow.geometry('300x200')
signupwindow.resizable(False,False)

signupwindow.configure(bg="teal") 
banner_label = Label(signupwindow, text="Signup Portal", fg="white", bg="#003366", font=("Arial", 16, "bold"))
banner_label.pack()

logindata = sqlite3.connect('users.db')
logindb = logindata.cursor()

def signup():
    username = usernameentry.get()
    password = passwordentry.get()
    if username and password:
        logindb.execute("SELECT * FROM users WHERE username=?", (username,))
        if logindb.fetchone():
            messagebox.showerror('Error', 'Username already exists')
        else:
            logindb.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            logindata.commit()
            usernameentry.delete(0,END)
            passwordentry.delete(0,END)
            messagebox.showinfo('Success', 'Account created successfully!')
            
            signupwindow.destroy()
    else:
        messagebox.showerror('Error', 'Please enter both username and password')
        signupwindow.destroy()


username = Label(signupwindow, text='Username:',bg="teal").place(x=40, y=50)
password = Label(signupwindow, text='Password:',bg="teal").place(x=40, y=75)

usernameentry = Entry(signupwindow)
usernameentry.place(x=120, y=50)


passwordentry = Entry(signupwindow)
passwordentry.place(x=120, y=75)
signupbutton = Button(signupwindow, text='Signup', fg='white', bg="#003366", command=signup)
signupbutton.place(x=120, y=100)

signupwindow.mainloop()
logindata.close()
