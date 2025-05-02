# with open("bright_words_done.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("bright_words_done.txt", "r") as file:
#     line = file.readline()
#     while line:
#         print(line, end='')
#         line = file.readline()


# with open("bright_words_done.txt", "r") as file:
#     lines = file.readline()
#     for line in lines:
#         print(line, end='')


# with open("bright_words_done.txt", "w") as file:
#     file.write("Hello, World!")
#     print ("Content added Successfully!!")


# lines = ["First line\n", "Second line\n", "Third line\n"]
# with open("bright_words_done.txt", "w") as file:
#     file.writelines(lines)
#     print ("Content added Successfully!!")


# file = open("example.txt", "a")
# file.write("Appending this line.\n")
# file.close()
# print("File opened successfully!!")

# import random
# import string

# def generate_password(length):
#     """"Generates a random password of given length."""
#     characters = string.ascii_letters + string.digits + string.punctuation
#     return "".join(random.choice(characters)for _ in range(length))

# def main():
#     """Prompts user for number of passwords and length, then generates them."""
#     try:
#         num_passwords = int(input("Enter the number of passwords to generate: ")) 
#         password_length = int(input("Enter the length of each password: "))

#         if num_passwords <= 0 or password_length <= 0:
#             print("Please enter positive numbers only.")
#             return

#         print("\nGenerated Password:")
#         for i in range(num_passwords):
#             print(f"{i+1}. {generate_password(password_length)}")
    
#     except ValueError:
#         print("Invalid input! Please enter numeric values.")

# if __name__ == "___main___":
#     main()

# if(True):
#     print("0")
#     if(True):
#         print("1")
# else:
#     print("2")


# import csv
# import os

# # Prompt for the CSV file  name
# file_name = input("Enter the name of the CSV file (with .csv extension): ")

# # Check if the file exists
# file_exists = os.path.isfile(file_name)

# if file_exists:
#     print("File exist.")
# else:
#     print("File does not exist. Creating file...")
#     # Create file with headers
#     with open(file_name, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["name", "age", "gender"])

# #Prompt for user details
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# gender = input("Enter your gender: ")

# # Append user details to the file with open(file_name, mode="a", newline="")as file:
# writer = csv.writer(file)
# writer.writerow(["name", "age", "gender"]) # Writing headers


# import random
# import string

# def generate_password(length):
#     """"Generates a random password of given length."""
#     Characters = string.ascii_letters + string.digits + string.punctuation 
#     return ''.join(random.choice(Characters) for _ in range(length))

# def main():
#     """Prompts user for number of passwords and length, then generates them."""
#     try:  
#         num_passwords = int(input("Enter the number of passwords to generate: "))
#         password_length = int(input("Enter the length of each password: "))
       
#         if num_passwords <= 0 or password_length <= 0:
#             print("please enter positive numbers only.")

#             return
#         print("\nGenerated Passwords:")
        
#         for i in range(num_passwords):
#             print(f"{i+1}.{generate_password(password_length)}")
            
#     except ValueError:
#         print("Invalid input! please enter numeric values.")
# if __name__ == "_main_":
#     main()

# with open("bright_word-done.txt", "r") as file:
#     for i, line in enumerate(file, start=): # Read the first 5th line
#         print(line) 


# import matplotlib.pyplot as plt
# # Create a new figure
# fig = plt.figure()

# # Add a plot or Subpot to the figure

# plt.plot([1, 2, 3], [4, 5, 6])
# plt.show()

# import tkinter as tk

# root = tk.Tk()

# root.title("WELCOME TO MY GUI")
# root.iconbitmap("IMG.ico")

# name = tk.Label(root, text="Enter your name")
# name.pack()

# name_entry = tk.Entry(root)
# name_entry.pack()

# root.mainloop()

# import tkinter as tk

# root = tk.Tk()

# root.title("WELCOME TO MY GUI")
# root.iconbitmap("IMG.ico")

# name = tk.Label(root, text="Enter your name")
# name.pack()

# name_entry = tk.Entry(root)
# name_entry.pack()

# root.mainloop()


# import tkinter as tk

# root = tk.Tk()

# root.title("WELCOME TO MY GUI")
# root.iconbitmap("IMG.ico")
# root.geometry("250x150")

# Frame1 = tk.Frame(root)
# Frame1.grid()
# name = tk.Label(Frame1, text="Enter your name")
# name.pack(side= "left", padx= 25, expand= True)


# name_entry = tk.Entry(Frame1)
# name_entry.pack(side= "right", padx=(0,25),expand= True)

# Frame2 = tk.Frame(root)
# Frame2.grid()
# password = tk.Label(Frame2, text= "Enter your Password")
# password.grid(row = 0, column= 0)

# password_entry = tk.Entry(Frame2)
# password_entry.grid(row = 0, column= 1)

# root.mainloop()


