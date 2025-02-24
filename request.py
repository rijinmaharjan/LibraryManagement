import sqlite3
from tkinter import messagebox



db = sqlite3.connect('requests.db')
cursor = db.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Requests(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Book_id INTEGER,
    Name TEXT,
    Author TEXT,
    Status TEXT,
    FOREIGN KEY(Book_id) REFERENCES Books(id)
    )'''
)
db.commit()


def add_request(book_list, requests_list):
    
    selected = book_list.curselection()
    if selected:
        book = book_list.get(selected[0])
        book_id = book.split('.')[0].strip()
        name = book.split(' by ')[0].split('.', 1)[1].strip()
        author = book.split(' by ')[1].split(' - ')[0].strip()
        
        cursor.execute("INSERT INTO Requests (Book_id, Name, Author, Status) VALUES (?, ?, ?, 'Pending')", 
                       (book_id, name, author))
        db.commit()
        
        request_text = f"{book_id}. {name} by {author} - Pending"
        if request_text not in requests_list.get(0, 'end'):
            requests_list.insert('end', request_text)
            messagebox.showinfo("Success", "Book requested!")
        else:
            messagebox.showwarning("Warning", "Already requested!")
    else:
        messagebox.showerror("Error", "Select a book first!")

def delete_request(book_id, name, author, requests_list):
    cursor.execute("DELETE FROM Requests WHERE Book_id = ? AND Name = ? AND Author = ?",
                   (book_id, name, author))
    db.commit()
    for i, request in enumerate(requests_list.get(0, 'end')):
        if request.startswith(f"{book_id}. {name} by {author}"):
            requests_list.delete(i)
            break

def show_requests(requests_list):
    cursor.execute("SELECT Book_id, Name, Author, Status FROM Requests")
    requests = cursor.fetchall()
    requests_list.delete(0, 'end')
    for book_id, name, author, status in requests:
        requests_list.insert('end', f"{book_id}. {name} by {author} - {status}")



def close_db():
    db.commit()
    db.close()