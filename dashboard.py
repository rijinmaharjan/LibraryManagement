from tkinter import *
from tkinter import messagebox
import sqlite3
import runpy



<<<<<<< HEAD

=======
>>>>>>> 72f559ad23588259b789d57daaf7f2b3911347ba
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



newbook_icon = PhotoImage(file="bookicon.png")
lendbook_icon = PhotoImage(file="lendbookicon.png")
returnbook_icon = PhotoImage(file="returnbookicon.png")
deletebook_icon = PhotoImage(file="deletebookicon.png") 
refreshbook_icon = PhotoImage(file="refreshbookicon.png") 
logout_icon = PhotoImage(file="logouticon.png")



menuframe = Frame(dashboard, height=50, bg='gray')
menuframe.pack(fill='x')



request_module = runpy.run_path('request.py')
lend_module = runpy.run_path('lend.py')
return_module = runpy.run_path('return.py')



def newbook():
    runpy.run_path('newbook.py')



def lendbook():
    lend_module['add_to_lent'](requests_list, borrowed_list, booklist_cursor)
    booklist_db.commit()  
<<<<<<< HEAD
    show_books()  

=======
    show_books() 
>>>>>>> 72f559ad23588259b789d57daaf7f2b3911347ba


def request_book():
    request_module['add_request'](book_list, requests_list)

<<<<<<< HEAD
def returnbook():
    return_module['return_book'](borrowed_list, requests_list, booklist_cursor)
    booklist_db.commit()  
    show_books() 

=======


def returnbook():
    return_module['return_book'](borrowed_list, requests_list, booklist_cursor)
    booklist_db.commit() 
    show_books()  
>>>>>>> 72f559ad23588259b789d57daaf7f2b3911347ba


def deletebook():
    
   
   
    selected_book = book_list.curselection()
    selected_request = requests_list.curselection()
    selected_lent = borrowed_list.curselection()
    
    if not (selected_book or selected_request or selected_lent):
        messagebox.showerror("Error", "Please select a book to delete!")
        return
    
    
    if selected_book:
        selected_item = book_list.get(selected_book[0])
    elif selected_request:
        selected_item = requests_list.get(selected_request[0])
    else: 
        selected_item = borrowed_list.get(selected_lent[0])
    
    book_id = selected_item.split('.')[0].strip()
    name = selected_item.split(' by ')[0].split('.', 1)[1].strip()
    author = selected_item.split(' by ')[1].split(' - ')[0].strip()
    
    

    booklist_cursor.execute("DELETE FROM Books WHERE id = ?", (book_id,))
    request_module['delete_request'](book_id, name, author, requests_list)
    lend_module['delete_lent'](book_id, name, author, borrowed_list)
    
    booklist_db.commit()
    
   

    show_books()
    request_module['show_requests'](requests_list)
    lend_module['show_lent'](borrowed_list)
    
    messagebox.showinfo("Success", f"Book '{name}' deleted from all records!")

def refreshbook():
    show_books()
    request_module['show_requests'](requests_list)
    lend_module['show_lent'](borrowed_list)

def logout():
    dashboard.destroy()
    runpy.run_path('loginpage.py')



newbook_button = Button(menuframe, text="New Book", image=newbook_icon, compound=LEFT, command=newbook)
newbook_button.grid(row=0, column=0, padx=5, pady=5)

returnbook_button = Button(menuframe, text="Request Book", image=returnbook_icon, compound=LEFT, command=request_book)
returnbook_button.grid(row=0, column=1, padx=5, pady=5)

lendbook_button = Button(menuframe, text="Lend Book", image=lendbook_icon, compound=LEFT, command=lendbook)
lendbook_button.grid(row=0, column=2, padx=5, pady=5)

return_button = Button(menuframe, text="Return Book", image=returnbook_icon, compound=LEFT, command=returnbook)
return_button.grid(row=0, column=3, padx=5, pady=5)

<<<<<<< HEAD
deletebook_button = Button(menuframe, text="Delete", image=deletebook_icon, compound=LEFT, command=deletebook)
=======
deletebook_button = Button(menuframe, text="Delete Selected Book", image=deletebook_icon, compound=LEFT, command=deletebook)
>>>>>>> 72f559ad23588259b789d57daaf7f2b3911347ba
deletebook_button.grid(row=0, column=4, padx=5, pady=5)

refreshbook_button = Button(menuframe, text="Refresh Book", image=refreshbook_icon, compound=LEFT, command=refreshbook)
refreshbook_button.grid(row=0, column=5, padx=5, pady=5)

logout_button = Button(menuframe, text="Logout", image=logout_icon, compound=LEFT, command=logout)
logout_button.grid(row=0, column=6, padx=5, pady=5)


<<<<<<< HEAD

=======
>>>>>>> 72f559ad23588259b789d57daaf7f2b3911347ba

main_frame = Frame(dashboard)
main_frame.pack(fill=BOTH, expand=True)



<<<<<<< HEAD

=======
>>>>>>> 72f559ad23588259b789d57daaf7f2b3911347ba
book_frame = Frame(main_frame, bg="#0a0102", width=300)
book_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

book_label = Label(book_frame, text="All Books", font=("Arial", 16, "bold"), bg="#0a0102")
book_label.pack(pady=5)

book_list = Listbox(book_frame, height=20, width=50, bg="white", fg='#0a0102')
book_list.pack(fill=BOTH, expand=True, padx=5, pady=5)


<<<<<<< HEAD


=======
>>>>>>> 72f559ad23588259b789d57daaf7f2b3911347ba
right_frame = Frame(main_frame, bg="#e6f3ff")
right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)


<<<<<<< HEAD


=======
>>>>>>> 72f559ad23588259b789d57daaf7f2b3911347ba
requests_frame = Frame(right_frame, bg="#0a0102")
requests_frame.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

requests_label = Label(requests_frame, text="Requests", font=("Arial", 16, "bold"), bg="#0a0102")
requests_label.pack(pady=5)

requests_list = Listbox(requests_frame, height=10, width=50, bg="white", fg='#0a0102')
requests_list.pack(fill=BOTH, expand=True, padx=5, pady=5)

<<<<<<< HEAD


=======
>>>>>>> 72f559ad23588259b789d57daaf7f2b3911347ba
borrowers_frame = Frame(right_frame, bg="#0a0102")
borrowers_frame.pack(side=BOTTOM, fill=BOTH, expand=True, padx=5, pady=5)

borrowers_label = Label(borrowers_frame, text="Your Borrowed Books", font=("Arial", 16, "bold"), bg="#0a0102")
borrowers_label.pack(pady=5)

borrowed_list = Listbox(borrowers_frame, height=10, width=50, bg="white", fg='#0a0102')
borrowed_list.pack(fill=BOTH, expand=True, padx=5, pady=5)

<<<<<<< HEAD


=======
>>>>>>> 72f559ad23588259b789d57daaf7f2b3911347ba
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
    return_module['close_db']()

closewindow_button = Button(dashboard, text='Close window', command=closewin)
closewindow_button.place(relx=1, rely=0, anchor='ne')



show_books()
request_module['show_requests'](requests_list)
lend_module['show_lent'](borrowed_list)

dashboard.mainloop()



booklist_db.commit()
booklist_db.close()
request_module['close_db']()
lend_module['close_db']()
return_module['close_db']()