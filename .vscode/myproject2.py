# Full Library Management System using Tkinter + PostgreSQL
# Requirements: psycopg2, tkinter, PIL (for profile pictures)
# Ensure your PostgreSQL DB is set up with appropriate tables first.

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import psycopg2
import hashlib
import os
import re

# --- Database Connection ---
def connect_db():
    return psycopg2.connect(
        dbname="your_database_name",     # e.g. "library_db"
        user="postgres",                 # PostgreSQL default user is lowercase "postgres"
        password="your_actual_password", # Must match your DB password
        host="localhost",
        port="5432"
    )



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# --- Global Variables ---
current_user = None

# --- App Window ---
app = tk.Tk()
app.title("Abia Open Source Library")
app.geometry("600x500")

# --- Utility ---
def clear_window():
    for widget in app.winfo_children():
        widget.destroy()

# --- Registration Form ---
def show_registration():
    clear_window()

    tk.Label(app, text="Register", font=("Arial", 20)).pack(pady=10)

    form_frame = tk.Frame(app)
    form_frame.pack(pady=10)

    entries = {}
    fields = ["First Name", "Last Name", "Email", "Gender", "Age", "Phone", "Home Address", "Username", "Password"]
    for field in fields:
        tk.Label(form_frame, text=field).pack(anchor="w")
        entry = tk.Entry(form_frame, show="*" if field == "Password" else None, width=40)
        entry.pack()
        entries[field] = entry

    is_librarian = tk.BooleanVar()
    tk.Checkbutton(form_frame, text="I am a librarian", variable=is_librarian).pack(pady=5, anchor="w")

    tk.Label(form_frame, text="Employment ID (if librarian)").pack(anchor="w")
    emp_id_entry = tk.Entry(form_frame, width=40)
    emp_id_entry.pack()

    tk.Label(form_frame, text="Profile Picture (path)").pack(anchor="w")
    pic_entry = tk.Entry(form_frame, width=40)
    pic_entry.pack()

    def submit():
        data = {field: entries[field].get() for field in fields}
        password = hash_password(data['Password'])

        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO users (first_name, last_name, email, gender, age, phone_number, home_address,
                username, password, profile_picture, is_librarian, employment_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                data['First Name'], data['Last Name'], data['Email'], data['Gender'], data['Age'],
                data['Phone'], data['Home Address'], data['Username'], password,
                pic_entry.get(), is_librarian.get(), emp_id_entry.get() if is_librarian.get() else None
            ))
            conn.commit()
            messagebox.showinfo("Success", "Registered Successfully")
            show_login()
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

    # ✅ Submit Button
    tk.Button(app, text="Submit Registration", command=submit, bg="green", fg="white", font=("Arial", 12)).pack(pady=10)

    tk.Button(app, text="Back to Login", command=show_login).pack()

# --- Login ---
def show_login():
    clear_window()
    tk.Label(app, text="Login", font=("Arial", 20)).pack(pady=10)

    tk.Label(app, text="Username or Email").pack()
    username_entry = tk.Entry(app)
    username_entry.pack()

    tk.Label(app, text="Password").pack()
    password_entry = tk.Entry(app, show="*")
    password_entry.pack()

    def login():
        global current_user
        identifier = username_entry.get()
        password = hash_password(password_entry.get())

        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("""
                SELECT id, first_name, is_librarian FROM users
                WHERE (username=%s OR email=%s) AND password=%s
            """, (identifier, identifier, password))
            user = cur.fetchone()

            if user:
                current_user = {'id': user[0], 'name': user[1], 'is_librarian': user[2]}
                messagebox.showinfo("Welcome", f"Hello {user[1]}")
                if user[2]:
                    show_librarian_dashboard()
                else:
                    show_user_dashboard()
            else:
                messagebox.showerror("Failed", "Invalid login")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

    tk.Button(app, text="Login", command=login).pack(pady=10)
    tk.Button(app, text="Register", command=show_registration).pack()

# --- User Dashboard ---
def show_user_dashboard():
    clear_window()
    tk.Label(app, text=f"Welcome, {current_user['name']} (User)", font=("Arial", 16)).pack(pady=10)

    tk.Button(app, text="Search Books", command=search_books).pack(pady=5)
    tk.Button(app, text="Borrow Book", command=borrow_book).pack(pady=5)
    tk.Button(app, text="Return Book", command=return_book).pack(pady=5)
    tk.Button(app, text="Donate Book", command=donate_book).pack(pady=5)
    tk.Button(app, text="Feedback", command=leave_feedback).pack(pady=5)
    tk.Button(app, text="Logout", command=show_login).pack(pady=20)

# --- Librarian Dashboard ---
def show_librarian_dashboard():
    clear_window()
    tk.Label(app, text=f"Welcome, {current_user['name']} (Librarian)", font=("Arial", 16)).pack(pady=10)

    tk.Button(app, text="Upload Book", command=upload_book).pack(pady=5)
    tk.Button(app, text="View Users & Borrowed Books", command=view_users_borrowed).pack(pady=5)
    tk.Button(app, text="Search Books", command=search_books).pack(pady=5)
    tk.Button(app, text="Logout", command=show_login).pack(pady=20)

# --- Placeholder Actions ---
def search_books():
    messagebox.showinfo("Search", "Search feature here")

def borrow_book():
    messagebox.showinfo("Borrow", "Borrow book feature here")

def return_book():
    messagebox.showinfo("Return", "Return book feature here")

def donate_book():
    messagebox.showinfo("Donate", "Donation feature pending librarian approval")

def leave_feedback():
    messagebox.showinfo("Feedback", "Feedback submission here")

def upload_book():
    messagebox.showinfo("Upload", "Book upload by librarian")

def view_users_borrowed():
    messagebox.showinfo("Borrowed List", "List of users & borrowed books")

# --- Start the App ---
show_login()
app.mainloop()
