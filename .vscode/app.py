import tkinter as tk
from tkinter import messagebox
import psycopg2
import hashlib

def register_user():
    conn = psycopg2.connect(
        dbname="library_db",
        user="your_username",
        password="your_password",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    first = entry_first.get()
    last = entry_last.get()
    email = entry_email.get()
    gender = entry_gender.get()
    age = entry_age.get()
    phone = entry_phone.get()
    address = entry_address.get()
    username = entry_username.get()
    password = hashlib.sha256(entry_password.get().encode()).hexdigest()
    is_librarian = var_librarian.get()
    employment_id = entry_empid.get() if is_librarian else None

    try:
        cur.execute("""
            INSERT INTO users (first_name, last_name, email, gender, age, phone_number, home_address,
            username, password, is_librarian, employment_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (first, last, email, gender, age, phone, address, username, password, is_librarian, employment_id))
        conn.commit()
        messagebox.showinfo("Success", "User registered successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        cur.close()
        conn.close()

# Tkinter GUI
app = tk.Tk()
app.title("Library Registration")
app.geometry("400x500")

tk.Label(app, text="First Name").pack()
entry_first = tk.Entry(app)
entry_first.pack()

tk.Label(app, text="Last Name").pack()
entry_last = tk.Entry(app)
entry_last.pack()

tk.Label(app, text="Email").pack()
entry_email = tk.Entry(app)
entry_email.pack()

tk.Label(app, text="Gender").pack()
entry_gender = tk.Entry(app)
entry_gender.pack()

tk.Label(app, text="Age").pack()
entry_age = tk.Entry(app)
entry_age.pack()

tk.Label(app, text="Phone").pack()
entry_phone = tk.Entry(app)
entry_phone.pack()

tk.Label(app, text="Address").pack()
entry_address = tk.Entry(app)
entry_address.pack()

tk.Label(app, text="Username").pack()
entry_username = tk.Entry(app)
entry_username.pack()

tk.Label(app, text="Password").pack()
entry_password = tk.Entry(app, show="*")
entry_password.pack()

var_librarian = tk.BooleanVar()
tk.Checkbutton(app, text="Are you a librarian?", variable=var_librarian).pack()

tk.Label(app, text="Employment ID (if librarian)").pack()
entry_empid = tk.Entry(app)
entry_empid.pack()

tk.Button(app, text="Register", command=register_user).pack(pady=20)

app.mainloop()
