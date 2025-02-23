from tkinter import *
from tkinter import messagebox
import sqlite3
import runpy
from PIL import Image, ImageTk 

# Database for books
booklist_db = sqlite3.connect('allbooks.db')
booklist_cursor = booklist_db.cursor()
booklist_cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Author TEXT,
    Status TEXT
    )'''
)

dashboard = Tk()
dashboard.attributes('-fullscreen', True)

# Icons for widget
newbook_icon = PhotoImage(file="bookicon.png")
lendbook_icon = PhotoImage(file="lendbookicon.png")
returnbook_icon = PhotoImage(file="returnbookicon.png")
deletebook_icon = PhotoImage(file="deletebookicon.png") 
refreshbook_icon = PhotoImage(file="refreshbookicon.png") 
logout_icon = PhotoImage(file="logouticon.png")

# Menu bar frame
menuframe = Frame(dashboard, height=50, bg='gray')
menuframe.pack(fill='x')

# Load modules
request_module = runpy.run_path('request.py')
lend_module = runpy.run_path('lend.py')

# Functions for menu buttons
def newbook():
    runpy.run_path('newbook.py')

def lendbook():
    lend_module['add_to_lent'](requests_list, borrowed_list, booklist_cursor)
    booklist_db.commit()  # Commit Books status change
    show_books()  # Refresh book_list

def request_book():
    request_module['add_request'](book_list, requests_list)

def deletebook():
    selected = book_list.curselection()
    if selected:
        selected_book = book_list.get(selected[0])
        book_id = selected_book.split('.')[0]
        booklist_cursor.execute("DELETE FROM Books WHERE id = ?", (book_id,))
        booklist_db.commit()
        show_books()
        messagebox.showinfo("Success", "Book deleted successfully!")
    else:
        messagebox.showerror("Error", "Please select a book to delete.")

def refreshbook():
    show_books()
    request_module['show_requests'](requests_list)
    lend_module['show_lent'](borrowed_list)

def logout():
    dashboard.destroy()
    runpy.run_path('loginpage.py')

# Menu buttons
newbook_button = Button(menuframe, text="New Book", image=newbook_icon, compound=LEFT, command=newbook)
newbook_button.grid(row=0, column=0, padx=5, pady=5)

returnbook_button = Button(menuframe, text="Request Book", image=returnbook_icon, compound=LEFT, command=request_book)
returnbook_button.grid(row=0, column=1, padx=5, pady=5)

lendbook_button = Button(menuframe, text="Lend Book", image=lendbook_icon, compound=LEFT, command=lendbook)
lendbook_button.grid(row=0, column=2, padx=5, pady=5)

deletebook_button = Button(menuframe, text="Delete Selected Book", image=deletebook_icon, compound=LEFT, command=deletebook)
deletebook_button.grid(row=0, column=3, padx=5, pady=5)

refreshbook_button = Button(menuframe, text="Refresh Book", image=refreshbook_icon, compound=LEFT, command=refreshbook)
refreshbook_button.grid(row=0, column=4, padx=5, pady=5)

logout_button = Button(menuframe, text="Logout", image=logout_icon, compound=LEFT, command=logout)
logout_button.grid(row=0, column=5, padx=5, pady=5)

# Main frame
main_frame = Frame(dashboard)
main_frame.pack(fill=BOTH, expand=True)

# Book frame
book_frame = Frame(main_frame, bg="#0a0102", width=300)
book_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

book_label = Label(book_frame, text="All Books", font=("Arial", 16, "bold"), bg="#0a0102")
book_label.pack(pady=5)

book_list = Listbox(book_frame, height=20, width=50, bg="white", fg='#0a0102')
book_list.pack(fill=BOTH, expand=True, padx=5, pady=5)

# Right frame
right_frame = Frame(main_frame, bg="#e6f3ff")
right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)

# Requests frame
requests_frame = Frame(right_frame, bg="#0a0102")
requests_frame.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

requests_label = Label(requests_frame, text="Requests", font=("Arial", 16, "bold"), bg="#0a0102")
requests_label.pack(pady=5)

requests_list = Listbox(requests_frame, height=10, width=50, bg="white", fg='#0a0102')
requests_list.pack(fill=BOTH, expand=True, padx=5, pady=5)

# Borrowers frame
borrowers_frame = Frame(right_frame, bg="#0a0102")
borrowers_frame.pack(side=BOTTOM, fill=BOTH, expand=True, padx=5, pady=5)

borrowers_label = Label(borrowers_frame, text="Your Borrowed Books", font=("Arial", 16, "bold"), bg="#0a0102")
borrowers_label.pack(pady=5)

borrowed_list = Listbox(borrowers_frame, height=10, width=50, bg="white", fg='#0a0102')
borrowed_list.pack(fill=BOTH, expand=True, padx=5, pady=5)

# Show books
def show_books():
    booklist_cursor.execute('SELECT * FROM Books')
    result = booklist_cursor.fetchall()
    book_list.delete(0, 'end')
    for book in result:
        book_list.insert('end', f"{book[0]}. {book[1]} by {book[2]} - {book[3]}")

def closewin():
    dashboard.destroy()
    booklist_db.commit()
    booklist_db.close()
    request_module['close_db']()
    lend_module['close_db']()

closewindow_button = Button(dashboard, text='Close window', command=closewin)
closewindow_button.place(relx=1, rely=0, anchor='ne')

# Load data on startup
show_books()
request_module['show_requests'](requests_list)
lend_module['show_lent'](borrowed_list)

dashboard.mainloop()

# Cleanup after main loop exits
booklist_db.commit()
booklist_db.close()
request_module['close_db']()
lend_module['close_db']()