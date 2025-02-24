import sqlite3
from tkinter import messagebox


<<<<<<< HEAD

=======
>>>>>>> 72f559ad23588259b789d57daaf7f2b3911347ba
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

def return_book(borrowed_list, requests_list, booklist_cursor):
    
    selected = borrowed_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select a book from the Lent part!")
        return

    selected_lent = borrowed_list.get(selected[0])
    book_id = selected_lent.split('.')[0].strip()
    name = selected_lent.split(' by ')[0].split('.', 1)[1].strip()
    author = selected_lent.split(' by ')[1].split(' - ')[0].strip()

<<<<<<< HEAD


=======
    
>>>>>>> 72f559ad23588259b789d57daaf7f2b3911347ba
    cursor.execute("DELETE FROM Lent WHERE Book_id = ? AND Name = ? AND Author = ?",
                   (book_id, name, author))
    db.commit()

<<<<<<< HEAD
   

    borrowed_list.delete(selected[0])

   
   
=======
    
    borrowed_list.delete(selected[0])

    
>>>>>>> 72f559ad23588259b789d57daaf7f2b3911347ba
    for i, request in enumerate(requests_list.get(0, 'end')):
        if request.startswith(f"{book_id}. {name} by {author}"):
            requests_list.delete(i)
            break

    
<<<<<<< HEAD

    booklist_cursor.execute("UPDATE Books SET Status = 'Available' WHERE id = ?", (book_id,))
    messagebox.showinfo("Success", f"Book '{name}' returned!")


=======
    booklist_cursor.execute("UPDATE Books SET Status = 'Available' WHERE id = ?", (book_id,))
    messagebox.showinfo("Success", f"Book '{name}' returned!")

>>>>>>> 72f559ad23588259b789d57daaf7f2b3911347ba
def show_lent(borrowed_list):
    cursor.execute("SELECT Book_id, Name, Author, Status FROM Lent")
    lent_books = cursor.fetchall()
    borrowed_list.delete(0, 'end')
    for book_id, name, author, status in lent_books:
        borrowed_list.insert('end', f"{book_id}. {name} by {author} - {status}")

<<<<<<< HEAD



=======
>>>>>>> 72f559ad23588259b789d57daaf7f2b3911347ba
def close_db():
    db.commit()
    db.close()