from tkinter import *
from tkinter import messagebox
import sqlite3

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



def exit_fullscreen(event):
    login.attributes("-fullscreen",False)
login.bind('<Escape>',exit_fullscreen)
login.mainloop()