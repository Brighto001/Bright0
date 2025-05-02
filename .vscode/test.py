import csv
import os

def get_csv_filename():
    filename = input("Enter the CSV file name (including .csv extension): ")
    if not filename.endswith(".csv"):
        filename += ".csv"
    return filename

def create_csv_file(filename):
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["First Name", "Last Name", "Age", "Gender"])

def append_to_csv(filename, first_name, last_name, age, gender):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([first_name, last_name, age, gender])

def main():
    filename = get_csv_filename()
    create_csv_file(filename)
    
    while True:
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        
        append_to_csv(filename, first_name, last_name, age, gender)
        
        cont = input("Do you want to add another entry? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Exiting the program. Data saved to", filename)
            break

if __name__ == "__main__":
    main()


import csv
import os
import tkinter as tk
from tkinter import messagebox

def create_csv_file():
    filename = entry_filename.get().strip()
    if not filename.endswith(".csv"):
        filename += ".csv"
    
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["First Name", "Last Name", "Age", "Gender"])
    
    messagebox.showinfo("Success", f"CSV file '{filename}' created successfully!")
    entry_filename.config(state=tk.DISABLED)
    btn_create.config(state=tk.DISABLED)
    entry_firstname.config(state=tk.NORMAL)
    entry_lastname.config(state=tk.NORMAL)
    entry_age.config(state=tk.NORMAL)
    entry_gender.config(state=tk.NORMAL)
    btn_submit.config(state=tk.NORMAL)

def append_to_csv():
    filename = entry_filename.get().strip()
    if not filename.endswith(".csv"):
        filename += ".csv"
    
    first_name = entry_firstname.get().strip()
    last_name = entry_lastname.get().strip()
    age = entry_age.get().strip()
    gender = entry_gender.get().strip()
    
    if not first_name or not last_name or not age or not gender:
        messagebox.showwarning("Warning", "All fields must be filled!")
        return
    
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([first_name, last_name, age, gender])
    
    messagebox.showinfo("Success", "Entry added successfully!")
    entry_firstname.delete(0, tk.END)
    entry_lastname.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_gender.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("CSV Entry Form")

# CSV File Name Input
tk.Label(root, text="CSV File Name:").grid(row=0, column=0)
entry_filename = tk.Entry(root)
entry_filename.grid(row=0, column=1)
btn_create = tk.Button(root, text="Create", command=create_csv_file)
btn_create.grid(row=0, column=2)

# User Data Inputs
tk.Label(root, text="First Name:").grid(row=1, column=0)
entry_firstname = tk.Entry(root, state=tk.DISABLED)
entry_firstname.grid(row=1, column=1)

tk.Label(root, text="Last Name:").grid(row=2, column=0)
entry_lastname = tk.Entry(root, state=tk.DISABLED)
entry_lastname.grid(row=2, column=1)

tk.Label(root, text="Age:").grid(row=3, column=0)
entry_age = tk.Entry(root, state=tk.DISABLED)
entry_age.grid(row=3, column=1)

tk.Label(root, text="Gender:").grid(row=4, column=0)
entry_gender = tk.Entry(root, state=tk.DISABLED)
entry_gender.grid(row=4, column=1)

# Submit Button
btn_submit = tk.Button(root, text="Submit", command=append_to_csv, state=tk.DISABLED)
btn_submit.grid(row=5, column=1)

root.mainloop()



