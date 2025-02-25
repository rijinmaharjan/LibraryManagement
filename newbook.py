from tkinter import *
from tkinter import messagebox
import sqlite3

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    if title and author:
        conn = sqlite3.connect('allbooks.db')
        c = conn.cursor()
        c.execute("INSERT INTO Books (Name, Author, Status) VALUES (?, ?, ?)", (title, author, "Available"))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Book added successfully!")
        new_book.destroy()
        
        
    else:
        messagebox.showerror("Error", "Please fill in all fields")

new_book = Tk()
new_book.title("Add New Book")
new_book.geometry("300x200")
new_book.configure(bg='teal')
banner_label = Label(new_book, text="Add a New Book", fg="white", bg="#003366", font=("Arial", 16, "bold"))
banner_label.pack()

Label(new_book, text="Title:",bg='teal').pack()
title_entry = Entry(new_book)
title_entry.pack()

Label(new_book, text="Author:",bg='teal').pack()
author_entry = Entry(new_book)
author_entry.pack()

add_button = Button(new_book, text="Add Book",bg='lavender', command=add_book)
add_button.pack(pady=10)

new_book.mainloop()