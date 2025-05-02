import tkinter as tk
from tkinter import messagebox
import psycopg2
import hashlib

# Connect to DB
def connect_db():
    return psycopg2.connect(
        dbname="library_db",
        user="your_username",
        password="your_password",
        host="localhost",
        port="5432"
    )

# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Login handler
def login_user():
    identifier = entry_username.get()
    password = hash_password(entry_password.get())

    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT first_name, is_librarian FROM users
            WHERE (username=%s OR email=%s) AND password=%s
        """, (identifier, identifier, password))

        user = cur.fetchone()
        if user:
            name, is_librarian = user
            role = "Librarian" if is_librarian else "User"
            messagebox.showinfo("Login Successful", f"Welcome {name} ({role})!")
            window.destroy()  # Close login window
            # TODO: open user or librarian dashboard
        else:
            messagebox.showerror("Login Failed", "Invalid username/email or password.")

    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        cur.close()
        conn.close()

# Tkinter window
window = tk.Tk()
window.title("Library Login")
window.geometry("350x250")

tk.Label(window, text="Username or Email").pack(pady=5)
entry_username = tk.Entry(window)
entry_username.pack()

tk.Label(window, text="Password").pack(pady=5)
entry_password = tk.Entry(window, show="*")
entry_password.pack()

tk.Button(window, text="Login", command=login_user).pack(pady=20)

window.mainloop()
