from tkinter import *
from tkinter import messagebox
import sqlite3
import runpy
from PIL import Image, ImageTk 

# Database connection
def create_database():
    booklist = sqlite3.connect('allbooks.db')
    books = booklist.cursor()
    books.execute('''CREATE TABLE IF NOT EXISTS Books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name text,
        Author text,
        Status text
    )''')
    booklist.commit()
    return booklist, books

booklist, books = create_database()

# Create dashboard window
dashboard = Tk()
dashboard.attributes('-fullscreen', True)

# Set the background color for the entire dashboard window
dashboard.config(bg='lightcyan')  # Change to your desired background color

# Load icons for buttons
newbook_icon = PhotoImage(file="bookicon.png")
lendbook_icon = PhotoImage(file="lendbookicon.png")
returnbook_icon = PhotoImage(file="returnbookicon.png")
deletebook_icon = PhotoImage(file="deletebookicon.png")
refreshbook_icon = PhotoImage(file="refreshbookicon.png")
logout_icon = PhotoImage(file="logouticon.png")

# Menu frame with background color
menuframe = Frame(dashboard, height=50, bg='lightblue')  # Light blue background for menu
menuframe.pack(fill='x')

# Functions for the menu frame buttons
def newbook():
    runpy.run_path('newbook.py')

def lendbook():
    runpy.run_path('lendbook.py')

def returnbook():
    runpy.run_path('returnbook.py')

def deletebook():
    selected = book_list.curselection()
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

# Add color to menu buttons
newbook_button = Button(menuframe, text="New Book", image=newbook_icon, compound=LEFT, command=newbook, bg='green', fg='white')
newbook_button.grid(row=0, column=0, padx=5, pady=5)

lendbook_button = Button(menuframe, text="Lend Book", image=lendbook_icon, compound=LEFT, command=lendbook, bg='blue', fg='white')
lendbook_button.grid(row=0, column=1, padx=5, pady=5)

returnbook_button = Button(menuframe, text="Return Book", image=returnbook_icon, compound=LEFT, command=returnbook, bg='yellow', fg='black')
returnbook_button.grid(row=0, column=2, padx=5, pady=5)

deletebook_button = Button(menuframe, text="Delete Selected Book", image=deletebook_icon, compound=LEFT, command=deletebook, bg='red', fg='white')
deletebook_button.grid(row=0, column=3, padx=5, pady=5)

refreshbook_button = Button(menuframe, text="Refresh Book", image=refreshbook_icon, compound=LEFT, command=refreshbook, bg='orange', fg='black')
refreshbook_button.grid(row=0, column=4, padx=5, pady=5)

logout_button = Button(menuframe, text="Logout", image=logout_icon, compound=LEFT, command=logout, bg='purple', fg='white')
logout_button.grid(row=0, column=5, padx=5, pady=5)

# Book list frame with background color
book_frame = Frame(dashboard, bg='lightgray')  # Background color for book list frame
book_frame.pack(side=LEFT)

# Book List Label with black background and white text
book_label = Label(book_frame, text="Book List", font=(16), bg='black', fg='white')  # Black background, white text
book_label.pack(pady=10)  # Padding for spacing

book_list = Listbox(book_frame, height=30, width=120, bg='white', fg='black')  # Listbox with white background and black text
book_list.pack(fill=BOTH, expand=True)

# Function to show the books in the listbox
def show_books():
    books.execute('SELECT * FROM Books')
    result = books.fetchall()
    
    book_list.delete(0, END)

    for i in result:
        book_list.insert(END, f"{i[0]}. {i[1]} by {i[2]} - {i[3]}")

# Borrowers section with background color
borrowersframe = Frame(dashboard, bg='lightyellow')  # Set background color for borrowers frame
borrowersframe.pack(side=RIGHT)

borrowers_label = Label(borrowersframe, text="Borrowers List", font=(16), bg='lightyellow', fg='black')  # Label with custom text color
borrowers_label.pack()

borrowers_list_label = Listbox(borrowersframe, height=30, width=50, bg='white', fg='black')  # Listbox with white background and black text
borrowers_list_label.pack()

# Close window button
def closewin():
    dashboard.destroy()

closewindowbutton = Button(dashboard, text='Close window', command=closewin, bg='red', fg='white')
closewindowbutton.place(relx=1, rely=0, anchor='ne')

# Show the books initially
show_books()

# Run the main loop of the application
dashboard.mainloop()

# Close the database connection
booklist.close()
