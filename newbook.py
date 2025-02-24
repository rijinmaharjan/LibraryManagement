from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    if title and author:
        conn = sqlite3.connect('allbooks.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS Books (Name TEXT, Author TEXT, Status TEXT)")
        c.execute("INSERT INTO Books (Name, Author, Status) VALUES (?, ?, ?)", (title, author, "Available"))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Book added successfully!")
        title_entry.delete(0, END)
        author_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Please fill in all fields")


new_book = Tk()
new_book.title("Add New Book")
new_book.geometry("400x300")
new_book.resizable(False, False)

global bg_img
bg_img = Image.open("nsplash.jpg")  
bg_img = bg_img.resize((400, 300), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_img)
background_label = Label(new_book, image=bg_photo)
background_label.place(relwidth=1, relheight=1)

global img
img = Image.open("loob.jpg")  
img = img.resize((50, 50), Image.Resampling.LANCZOS)
book_img = ImageTk.PhotoImage(img)
img_label = Label(new_book, image=book_img, bg="#D1E8E2")
img_label.pack(pady=5)

title_label = Label(new_book, text="Title:", font=("Arial", 12, "bold"), bg="#D1E8E2")
title_label.pack(pady=(10, 0))
title_entry = Entry(new_book, width=30, bg="#F6F6F6")
title_entry.pack(pady=5)

author_label = Label(new_book, text="Author:", font=("Arial", 12, "bold"), bg="#D1E8E2")
author_label.pack(pady=(10, 0))
author_entry = Entry(new_book, width=30, bg="#F6F6F6")
author_entry.pack(pady=5)

add_button = Button(new_book, text="Add Book", command=add_book, bg="#A1C6EA", fg="black", font=("Arial", 10, "bold"))
add_button.pack(pady=15)

new_book.mainloop()