# import sqlite3

# def init_db():
#     conn = sqlite3.connect("library.db")
#     cursor = conn.cursor()

#     cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name TEXT, last_name TEXT, email TEXT UNIQUE,
#         gender TEXT, age INTEGER, phone TEXT, address TEXT,
#         username TEXT UNIQUE, password TEXT,
#         profile_pic TEXT, is_librarian INTEGER,
#         employment_id TEXT
#     )''')

#     cursor.execute('''CREATE TABLE IF NOT EXISTS books (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT, author TEXT, year INTEGER,
#         isbn TEXT, age_bracket TEXT, is_donated INTEGER,
#         approved INTEGER
#     )''')

#     conn.commit()
#     conn.close()


# import sqlite3
# import getpass

# def register_user():
#     print("\n=== User Registration ===")
#     data = {
#         "first_name": input("First name: "),
#         "last_name": input("Last name: "),
#         "email": input("Email: "),
#         "gender": input("Gender: "),
#         "age": int(input("Age: ")),
#         "phone": input("Phone: "),
#         "address": input("Address: "),
#         "username": input("Username: "),
#         "password": getpass.getpass("Password: "),
#         "profile_pic": input("Profile picture filename: "),
#         "is_librarian": 0,
#         "employment_id": None
#     }

#     conn = sqlite3.connect("library.db")
#     cursor = conn.cursor()

#     try:
#         cursor.execute('''INSERT INTO users (
#             first_name, last_name, email, gender, age, phone, address,
#             username, password, profile_pic, is_librarian, employment_id
#         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#             tuple(data.values())
#         )
#         conn.commit()
#         print("✅ User registered successfully!")
#     except sqlite3.IntegrityError:
#         print("❌ Username or email already exists.")
#     finally:
#         conn.close()


# def login():
#     print("\n=== Login ===")
#     uname = input("Username or Email: ")
#     pwd = getpass.getpass("Password: ")

#     conn = sqlite3.connect("library.db")
#     cursor = conn.cursor()
#     cursor.execute('''SELECT * FROM users WHERE (username=? OR email=?) AND password=?''', (uname, uname, pwd))
#     user = cursor.fetchone()
#     conn.close()

#     if user:
#         print(f"✅ Welcome, {user[1]}!")
#         return user
#     else:
#         print("❌ Invalid login.")
#         return None
    
# import sqlite3

# def add_book():
#     print("\n=== Add Book (Librarian) ===")
#     title = input("Book Title: ")
#     author = input("Author: ")
#     year = int(input("Year: "))
#     isbn = input("ISBN: ")
#     age_bracket = input("Age Bracket (e.g., 12-18): ")

#     conn = sqlite3.connect("library.db")
#     cursor = conn.cursor()
#     cursor.execute('''INSERT INTO books (title, author, year, isbn, age_bracket, is_donated, approved)
#                       VALUES (?, ?, ?, ?, ?, 0, 1)''',
#                    (title, author, year, isbn, age_bracket))
#     conn.commit()
#     conn.close()
#     print("✅ Book added to the library.")


# from database import init_db
# from user import register_user, login
# from book import add_book

# def main():
#     init_db()

#     while True:
#         print("\n=== Abia Open Source Library ===")
#         print("1. Register")
#         print("2. Login")
#         print("3. Exit")
#         choice = input("Choose an option: ")

#         if choice == "1":
#             register_user()
#         elif choice == "2":
#             user = login()
#             if user:
#                 is_librarian = user[11]
#                 if is_librarian:
#                     print("Librarian Menu:")
#                     print("1. Add Book")
#                     print("2. Logout")
#                     if input("Choose an option: ") == "1":
#                         add_book()
#                 else:
#                     print("User Dashboard (in progress)...")
#         elif choice == "3":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid option.")

# # if __name__ == "__main__":
# #     main()

# Group 1:
# Team Name: Super Six
# Project: Library Management System.
# Project Description:
# Our team has been tasked with designing a library management system for a physical library.
# We call it Abia Open Source library.
# The library has two main users: library staff and registered members. We call them users.
# Registration and login:
# The User:
# The user will provided the following details on registration:
# First name
# Last name
# Email
# Gender
# Age
# Pone number
# Home address
# Username
# Password
# Picture (for profile)
# The Librarian will provide everything the user provides and also his employment id number (which should be in the form lib/three digits/two digits)
# LOG IN REQUIREMENTS
# The user:
# Username or email address and password
# The librarian:
# Username or email address and password
# PRIVILEGES:
# The User: the user will be able to do the following:
# 1. Login
# 2. Borrow books from the library
# 3. Return borrowed books
# 4. Give feedback to the library
# 5. Search for books on the library database
# 6. Donate books to the library pendin the approval of the librarian
# 7. See his dashboard detailing recent searches, books borrowed and their due date of return
# The Librarian:
# 1. Upload available books to the library
# Book description will be done with the following details:
# Book name
# Author’s name
# Year of publication
# Isbn
# Age bracket
# And book search can be conducted by any user with the above criteria.
# 2. See list of library users, the books they borrowed and due date of return
# Appropriate GUI should be used to display the system for ease of use.
	

# --- library_app.py ---

import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
from PIL import Image, ImageTk
import os
import datetime

# ===== DATABASE SETUP =====
def init_db():
    conn = sqlite3.connect("library.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fname TEXT, lname TEXT, email TEXT, gender TEXT, age INTEGER,
        phone TEXT, address TEXT, username TEXT UNIQUE, password TEXT,
        is_librarian INTEGER, emp_id TEXT, profile TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT, author TEXT, year INTEGER,
        isbn TEXT, age_bracket TEXT, status TEXT,
        donated_by TEXT, approved INTEGER DEFAULT 1
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS borrows (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER, book_id INTEGER,
        borrow_date TEXT, due_date TEXT,
        returned INTEGER DEFAULT 0
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER, comment TEXT, date TEXT
    )''')
    conn.commit()
    conn.close()


# ===== APP CLASS =====
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Abia Open Source Library")
        self.root.geometry("500x600")
        self.user = None
        init_db()
        self.main_menu()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear()
        tk.Label(self.root, text="Abia Open Source Library", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="Register", width=20, command=self.register).pack(pady=10)
        tk.Button(self.root, text="Login", width=20, command=self.login).pack(pady=10)

    def register(self):
        self.clear()
        tk.Label(self.root, text="Registeration Page", font=("Arial", 14)).pack(pady=10)
        fields = ['First Name', 'Last Name', 'Email', 'Gender', 'Age', 'Phone', 'Address', 'Username', 'Password']
        entries = {}
        for field in fields:
            tk.Label(self.root, text=field).pack()
            entries[field] = tk.Entry(self.root)
            entries[field].pack()

        is_librarian = tk.IntVar()
        tk.Checkbutton(self.root, text="Register as Librarian", variable=is_librarian).pack()
        emp_entry = tk.Entry(self.root)
        tk.Label(self.root, text="Employment ID (if Librarian)").pack()
        emp_entry.pack()

        def submit():
            data = {f: entries[f].get() for f in fields}
            profile = filedialog.askopenfilename(title="Select Profile Image")
            conn = sqlite3.connect("library.db")
            c = conn.cursor()
            try:
                c.execute('''INSERT INTO users
                    (fname, lname, email, gender, age, phone, address, username, password, is_librarian, emp_id, profile)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (data['First Name'], data['Last Name'], data['Email'], data['Gender'],
                     int(data['Age']), data['Phone'], data['Address'], data['Username'],
                     data['Password'], is_librarian.get(), emp_entry.get(), profile))
                conn.commit()
                messagebox.showinfo("Success", "Registration complete.")
                self.main_menu()
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                conn.close()

        tk.Button(self.root, text="Submit", command=submit).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def login(self):
        self.clear()
        tk.Label(self.root, text="Login", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Username or Email").pack()
        uname_entry = tk.Entry(self.root)
        uname_entry.pack()
        tk.Label(self.root, text="Password").pack()
        pwd_entry = tk.Entry(self.root, show="*")
        pwd_entry.pack()

        def do_login():
            uname = uname_entry.get()
            pwd = pwd_entry.get()
            conn = sqlite3.connect("library.db")
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE (username=? OR email=?) AND password=?", (uname, uname, pwd))
            user = c.fetchone()
            conn.close()
            if user:
                self.user = user
                if user[11]:  # is_librarian
                    self.librarian_dashboard()
                else:
                    self.user_dashboard()
            else:
                messagebox.showerror("Error", "Invalid login.")

        tk.Button(self.root, text="Login", command=do_login).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def librarian_dashboard(self):
        self.clear()
        tk.Label(self.root, text="Librarian Dashboard", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Upload Book", command=self.upload_book).pack(pady=5)
        tk.Button(self.root, text="View Users & Borrows", command=self.view_borrows).pack(pady=5)
        tk.Button(self.root, text="Approve Donations", command=self.approve_books).pack(pady=5)
        tk.Button(self.root, text="View Feedback", command=self.view_feedback).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.main_menu).pack(pady=10)

    def upload_book(self):
        self.clear()
        tk.Label(self.root, text="Upload Book", font=("Arial", 14)).pack(pady=10)
        fields = ['Title', 'Author', 'Year', 'ISBN', 'Age Bracket']
        entries = {}
        for field in fields:
            tk.Label(self.root, text=field).pack()
            entries[field] = tk.Entry(self.root)
            entries[field].pack()

        def submit():
            conn = sqlite3.connect("library.db")
            c = conn.cursor()
            c.execute('''INSERT INTO books (title, author, year, isbn, age_bracket, status, donated_by)
                         VALUES (?, ?, ?, ?, ?, ?, ?)''',
                      (entries['Title'].get(), entries['Author'].get(), int(entries['Year'].get()),
                       entries['ISBN'].get(), entries['Age Bracket'].get(), "available", None))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Book uploaded.")
            self.librarian_dashboard()

        tk.Button(self.root, text="Submit", command=submit).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.librarian_dashboard).pack()

    def view_borrows(self):
        self.clear()
        tk.Label(self.root, text="Borrowed Books", font=("Arial", 14)).pack()
        text = tk.Text(self.root)
        text.pack()
        conn = sqlite3.connect("library.db")
        c = conn.cursor()
        c.execute('''SELECT u.username, b.title, br.borrow_date, br.due_date, br.returned
                     FROM borrows br
                     JOIN users u ON u.id = br.user_id
                     JOIN books b ON b.id = br.book_id''')
        rows = c.fetchall()
        for r in rows:
            status = "Returned" if r[4] else "Borrowed"
            text.insert(tk.END, f"{r[0]} - {r[1]} ({status})\nDue: {r[3]}\n\n")
        conn.close()
        tk.Button(self.root, text="Back", command=self.librarian_dashboard).pack(pady=5)

    def approve_books(self):
        self.clear()
        tk.Label(self.root, text="Approve Donations", font=("Arial", 14)).pack()
        listbox = tk.Listbox(self.root, width=50)
        listbox.pack()
        conn = sqlite3.connect("library.db")
        c = conn.cursor()
        c.execute("SELECT id, title FROM books WHERE approved=0")
        books = c.fetchall()
        for b in books:
            listbox.insert(tk.END, f"{b[0]}: {b[1]}")
        conn.close()

        def approve():
            selected = listbox.get(listbox.curselection())
            book_id = int(selected.split(":")[0])
            conn = sqlite3.connect("library.db")
            c = conn.cursor()
            c.execute("UPDATE books SET approved=1 WHERE id=?", (book_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Approved", "Book approved!")
            self.approve_books()

        tk.Button(self.root, text="Approve Selected", command=approve).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.librarian_dashboard).pack()

    def view_feedback(self):
        self.clear()
        tk.Label(self.root, text="User Feedback", font=("Arial", 14)).pack()
        text = tk.Text(self.root)
        text.pack()
        conn = sqlite3.connect("library.db")
        c = conn.cursor()
        c.execute("SELECT u.username, f.comment FROM feedback f JOIN users u ON f.user_id = u.id")
        for row in c.fetchall():
            text.insert(tk.END, f"{row[0]}: {row[1]}\n\n")
        conn.close()
        tk.Button(self.root, text="Back", command=self.librarian_dashboard).pack()

    def user_dashboard(self):
        self.clear()
        tk.Label(self.root, text=f"Welcome {self.user[8]}", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Search Books", command=self.search_books).pack(pady=5)
        tk.Button(self.root, text="Borrow Book", command=self.borrow_book).pack(pady=5)
        tk.Button(self.root, text="Return Book", command=self.return_book).pack(pady=5)
        tk.Button(self.root, text="Donate Book", command=self.donate_book).pack(pady=5)
        tk.Button(self.root, text="Give Feedback", command=self.give_feedback).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.main_menu).pack(pady=10)

    def search_books(self):
        self.clear()
        tk.Label(self.root, text="Search Books", font=("Arial", 14)).pack()
        entry = tk.Entry(self.root)
        entry.pack()
        text = tk.Text(self.root)
        text.pack()

        def search():
            conn = sqlite3.connect("library.db")
            c = conn.cursor()
            q = entry.get()
            c.execute('''SELECT title, author, year FROM books WHERE
                         title LIKE ? OR author LIKE ? OR isbn LIKE ?''', (f'%{q}%',)*3)
            books = c.fetchall()
            text.delete("1.0", tk.END)
            for b in books:
                text.insert(tk.END, f"{b[0]} by {b[1]} ({b[2]})\n")
            conn.close()

        tk.Button(self.root, text="Search", command=search).pack()
        tk.Button(self.root, text="Back", command=self.user_dashboard).pack()

    def borrow_book(self):
        self.clear()
        tk.Label(self.root, text="Borrow Book by Title", font=("Arial", 14)).pack()
        entry = tk.Entry(self.root)
        entry.pack()

        def borrow():
            title = entry.get()
            conn = sqlite3.connect("library.db")
            c = conn.cursor()
            c.execute("SELECT id FROM books WHERE title=? AND status='available' AND approved=1", (title,))
            book = c.fetchone()
            if book:
                today = datetime.date.today()
                due = today + datetime.timedelta(days=14)
                c.execute('''INSERT INTO borrows (user_id, book_id, borrow_date, due_date)
                             VALUES (?, ?, ?, ?)''', (self.user[0], book[0], today.isoformat(), due.isoformat()))
                c.execute("UPDATE books SET status='borrowed' WHERE id=?", (book[0],))
                conn.commit()
                messagebox.showinfo("Success", "Book borrowed.")
            else:
                messagebox.showerror("Error", "Book not available.")
            conn.close()
            self.user_dashboard()

        tk.Button(self.root, text="Borrow", command=borrow).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.user_dashboard).pack()

    def return_book(self):
        self.clear()
        tk.Label(self.root, text="Return Book by Title", font=("Arial", 14)).pack()
        entry = tk.Entry(self.root)
        entry.pack()

        def do_return():
            title = entry.get()
            conn = sqlite3.connect("library.db")
            c = conn.cursor()
            c.execute('''SELECT b.id FROM books b
                         JOIN borrows br ON b.id = br.book_id
                         WHERE b.title=? AND br.user_id=? AND br.returned=0''',
                      (title, self.user[0]))
            book = c.fetchone()
            if book:
                c.execute("UPDATE borrows SET returned=1 WHERE book_id=? AND user_id=?", (book[0], self.user[0]))
                c.execute("UPDATE books SET status='available' WHERE id=?", (book[0],))
                conn.commit()
                messagebox.showinfo("Success", "Book returned.")
            else:
                messagebox.showerror("Error", "Book not found or not borrowed.")
            conn.close()
            self.user_dashboard()

        tk.Button(self.root, text="Return", command=do_return).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.user_dashboard).pack()

    def donate_book(self):
        self.clear()
        tk.Label(self.root, text="Donate a Book", font=("Arial", 14)).pack()
        fields = ['Title', 'Author', 'Year', 'ISBN', 'Age Bracket']
        entries = {}
        for f in fields:
            tk.Label(self.root, text=f).pack()
            entries[f] = tk.Entry(self.root)
            entries[f].pack()

        def submit():
            conn = sqlite3.connect("library.db")
            c = conn.cursor()
            c.execute('''INSERT INTO books (title, author, year, isbn, age_bracket, status, donated_by, approved)
                         VALUES (?, ?, ?, ?, ?, ?, ?, 0)''',
                      (entries['Title'].get(), entries['Author'].get(), int(entries['Year'].get()),
                       entries['ISBN'].get(), entries['Age Bracket'].get(), "available", self.user[8]))
            conn.commit()
            conn.close()
            messagebox.showinfo("Thank you!", "Donation submitted for approval.")
            self.user_dashboard()

        tk.Button(self.root, text="Donate", command=submit).pack()
        tk.Button(self.root, text="Back", command=self.user_dashboard).pack()

    def give_feedback(self):
        self.clear()
        tk.Label(self.root, text="Your Feedback", font=("Arial", 14)).pack()
        text = tk.Text(self.root, height=10)
        text.pack()

        def send():
            comment = text.get("1.0", tk.END).strip()
            if comment:
                conn = sqlite3.connect("library.db")
                c = conn.cursor()
                c.execute("INSERT INTO feedback (user_id, comment, date) VALUES (?, ?, ?)",
                          (self.user[0], comment, datetime.date.today().isoformat()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Thank you", "Feedback submitted.")
            self.user_dashboard()

        tk.Button(self.root, text="Submit", command=send).pack()
        tk.Button(self.root, text="Back", command=self.user_dashboard).pack()


# ===== RUN APP =====
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
