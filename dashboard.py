from tkinter import *
from tkinter import messagebox
import sqlite3
import runpy
from PIL import Image, ImageTk 

#database for books
booklist= sqlite3.connect('allbooks.db')
books= booklist.cursor()
books.execute(
    '''CREATE TABLE IF NOT EXISTS Books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name text,
    Author text,
    Status text
    )
    '''
)



dashboard=Tk()
dashboard.attributes('-fullscreen',True)


#icons for widget
newbook_icon = PhotoImage(file="bookicon.png")
lendbook_icon = PhotoImage(file="lendbookicon.png")
returnbook_icon = PhotoImage(file="returnbookicon.png")
deletebook_icon = PhotoImage(file="deletebookicon.png") 
refreshbook_icon = PhotoImage(file="refreshbookicon.png") 
logout_icon = PhotoImage(file="logouticon.png")

#to create a menu bar frame at top
menuframe=Frame(dashboard,height=50,bg='gray')
menuframe.pack(fill='x')

#functions for the menu frame buttons
def newbook():
    runpy.run_path('newbook.py')

def lendbook():
    runpy.run_path('newbook.py')
def returnbook():
    runpy.run_path('newbook.py')


#to select and delete a book (we use split as it gives value before .)
def deletebook():
    selected=book_list.curselection()
    if selected:
        selected_book = book_list.get(selected[0])
        book_id = selected_book.split('.')[0]
        
        
        books.execute("DELETE FROM Books WHERE id = ?", (book_id,))
        booklist.commit()

        
        show_books()

    
        messagebox.showinfo("Success", "Book deleted successfully!")
    else:
       
        messagebox.showerror("Error", "Please select a book to delete.")

def refreshbook():
    show_books()
def logout():
    dashboard.destroy()
    runpy.run_path('loginpage.py')


#adding the menus on the frame
newbook_button = Button(menuframe, text="New Book",image=newbook_icon, compound=LEFT,command=newbook)
newbook_button.grid(row=0,column=0,padx=5, pady=5)

lendbook_button = Button(menuframe, text="Lend Book",image=lendbook_icon,compound=LEFT, command=lendbook)
lendbook_button.grid( row=0, column=1, padx=5, pady=5)

returnbook_button = Button(menuframe, text="Return Book", image=refreshbook_icon,compound=LEFT,command=returnbook)
returnbook_button.grid(row=0, column=2, padx=5, pady=5)

deletebook_button = Button(menuframe, text="Delete Selected Book", image=deletebook_icon,compound=LEFT,command=deletebook)
deletebook_button.grid(row=0, column=3, padx=5, pady=5)

refreshbook_button=Button(menuframe, text="Refresh Book",image=refreshbook_icon,compound=LEFT, command=refreshbook)
refreshbook_button.grid(row=0, column=4, padx=5, pady=5)

logout_button = Button(menuframe, text="Logout",image=logout_icon,compound=LEFT, command=logout)
logout_button.grid(row=0, column=5, padx=5, pady=5)

# book list frame
book_frame = Frame(dashboard)
book_frame.pack(side=LEFT)


book_label = Label(book_frame, text="Book List", font=(16))
book_label.pack()


book_list = Listbox(book_frame, height=30, width=120)
book_list.pack(fill=BOTH, expand=True) #fill both means both x and y fill total space and expand true menas to expand to all empty spaces

#to show the books in listbox of books
def show_books():
    books.execute('SELECT * FROM Books')
    result = books.fetchall()

    #if we do not deleted it will show same agin and again
    book_list.delete(0, END)

    for i in result:
        book_list.insert(END, f"{i[0]}. {i[1]} by {i[2]} - {i[3]}")


#section for borrowers
borrowersframe = Frame(dashboard)
borrowersframe.pack(side=RIGHT)

borrowers_label = Label(borrowersframe, text="Borrowers List", font=(16))
borrowers_label.pack()

borrowers_list_label = Listbox(borrowersframe,height=30, width=50)
borrowers_list_label.pack()


def closewin():
    dashboard.destroy()
closewindowbutton= Button(dashboard,text='Close window', command=closewin)
closewindowbutton.place(relx=1,rely=0,anchor='ne')

show_books()
dashboard.mainloop()
booklist.close()