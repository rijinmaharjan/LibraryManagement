from tkinter import *
from tkinter import messagebox
import sqlite3
import runpy
from PIL import Image, ImageTk

#for signin and signup initializing database
logindata = sqlite3.connect('users.db')
login=logindata.cursor()
login.execute(
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
login.minsize(400,400)

#for backgtound image
backgroundimage=Image.open('loginpage.jpg')
backgroundimage=backgroundimage.resize((login.winfo_screenwidth(), login.winfo_screenheight()))    #to resize with exact dimensions of my screen
backgroumdimage_insert = ImageTk.PhotoImage(backgroundimage) 
backgroundimage_label = Label(login, image=backgroumdimage_insert)
backgroundimage_label.place(x=0, y=0, relwidth=1, relheight=1)

#title for the page
banner_frame = Frame(login, bg="#003366", height=50)
banner_frame.pack() 
banner_label = Label(banner_frame, text="Library Management System Login Portal", fg="white", bg="#003366", font=("Arial", 16, "bold"))
banner_label.pack()

#for login frame 
screen_width = login.winfo_screenwidth()
screen_height = login.winfo_screenheight()


frame_width = 300 
frame_height = 200
x_center = (screen_width-frame_width) // 2
y_center = (screen_height-frame_height) // 2

frame = Frame(login, width=frame_width, height=frame_height,bg="#57a1f8")
frame.place(relx=0.5, rely=0.5, anchor='center', width=frame_width, height=frame_height)


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
    login.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if login.fetchone():
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
        login.execute("SELECT * FROM users WHERE username=?", (username,))
        if login.fetchone():
            messagebox.showerror('Error', 'Username already exists')
        else:
            login.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            logindata.commit()
            usernameentry.delete(0,END)
            passwordentry.delete(0,END)
            messagebox.showinfo('Success', 'Account created successfully!')
    else:
        messagebox.showerror('Error', 'Please enter both username and password')


username = Label(frame, text='Username:',bg="#57a1f8").place(x=40, y=50)
password = Label(frame, text='Password:',bg="#57a1f8").place(x=40, y=75)

usernameentry = Entry(frame)
usernameentry.place(x=120, y=50)


passwordentry = Entry(frame, show='*')
passwordentry.place(x=120, y=75)

checkbutton = IntVar()
showpasswordbutton = Checkbutton(frame, text='Show Password', bg="#57a1f8", variable=checkbutton, command=showpassword)
showpasswordbutton.place(x=75, y=100)

loginbutton = Button(frame, text='Login', fg='white', bg="#003366", command=signin)
loginbutton.place(x=85, y=120)

signupbutton = Button(frame, text='Signup', fg='white', bg="#003366", command=signup)
signupbutton.place(x=85, y=150)

#toclose the login window
def closewin():
    login.destroy()
closewindowbutton= Button(login,text='Close window', command=closewin)
closewindowbutton.place(relx=1,rely=0,anchor='ne')

#to exit full screen
def exit_fullscreen(event):
    login.attributes("-fullscreen",False)

#adding return bind so that enter thichda chalos
login.bind('<Return>',lambda event: signin())

login.bind('<Escape>',exit_fullscreen)
login.mainloop()
logindata.close()