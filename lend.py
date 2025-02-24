import sqlite3
from tkinter import messagebox



db = sqlite3.connect('lent.db')
cursor = db.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Lent(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Book_id INTEGER,
    Name TEXT,
    Author TEXT,
    Status TEXT,
    FOREIGN KEY(Book_id) REFERENCES Books(id)
    )'''
)
db.commit()


def add_to_lent(requests_list, borrowed_list, booklist_cursor):
    
    selected = requests_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select a book from the Requests list!")
        return

    selected_request = requests_list.get(selected[0])
    if "Pending" not in selected_request:
        messagebox.showerror("Error", "Selected request must be Pending!")
        return

    book_id, name_author = selected_request.split(' by ')
    book_id, name = book_id.split('.', 1)
    author = name_author.split(' - ')[0]
    lent_book = f"{book_id.strip()}. {name.strip()} by {author.strip()} - Lent Out"

    if lent_book in borrowed_list.get(0, 'end'):
        messagebox.showwarning("Warning", "This book is already lent out!")
        return

    cursor.execute("INSERT INTO Lent (Book_id, Name, Author, Status) VALUES (?, ?, ?, 'Lent Out')",
                   (book_id.strip(), name.strip(), author.strip()))
    db.commit()
    
    borrowed_list.insert('end', lent_book)
    requests_list.delete(selected[0])
    requests_list.insert(selected[0], lent_book)

    booklist_cursor.execute("UPDATE Books SET Status = 'Unavailable' WHERE id = ?", (book_id,))
    messagebox.showinfo("Success", f"Book '{name.strip()}' lent out!")

<<<<<<< HEAD
def delete_lent(book_id, name, author, borrowed_list):
    cursor.execute("DELETE FROM Lent WHERE Book_id = ? AND Name = ? AND Author = ?",
                   (book_id, name, author))
    db.commit()
    for i, lent in enumerate(borrowed_list.get(0, 'end')):
        if lent.startswith(f"{book_id}. {name} by {author}"):
            borrowed_list.delete(i)
            break
=======

>>>>>>> 72f559ad23588259b789d57daaf7f2b3911347ba

def show_lent(borrowed_list):
    cursor.execute("SELECT Book_id, Name, Author, Status FROM Lent")
    lent_books = cursor.fetchall()
    borrowed_list.delete(0, 'end')
    for book_id, name, author, status in lent_books:
        borrowed_list.insert('end', f"{book_id}. {name} by {author} - {status}")



def close_db():
    db.commit()
    db.close()