from tkinter import *
import sqlite3
import runpy

dashboard=Tk()
dashboard.attributes('-fullscreen',True)

#to create a menu bar frame at top
menuframe=Frame(dashboard,height=50,bg='gray')
menuframe.pack(fill='x')

#adding the menus on the frame
newbook=
new_library_member=
lendbook=
retunbook=




def closewin():
    dashboard.destroy()
closewindowbutton= Button(dashboard,text='Close window', command=closewin)
closewindowbutton.place(relx=1,rely=0,anchor='ne')
dashboard.mainloop()