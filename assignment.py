# name = input("Ogbonna Chimezie Bright")
# print(f"Good Morning {name}. How are you doing?") 

# # Calling the function
# compare_and_subtract(A, B)

# def calculate_mean():
#     numbers = []
#     for i in range(5):
#         num = float(input(f"enter number {i+1}: "))
#         numbers.append(num)
    
#     mean =  sum(numbers) / len(numbers)
#     return str(mean)

# result = calculate_mean()
# print("The mean is: " + result)

# def unicode_difference(letter: str) -> int:
#     return ord(letter.lower()) - ord(letter.upper())

# # Example: Using letter 'A' (you can replace it with any letter)
# letter = input("enter any letter (A-Z or a-z): ")
# difference = unicode_difference(letter)
# print("the difference in Unicode values is:", difference)

# import os

# # Set the folder path where your images are stored
# folder_path = r"C: \Users\YourUsername\Pictures"   #Change this to your actual folder path

# # Check if the folder exists
# if not os.path.exists(folder_path):
#     print(f"Error: The folder path '{folder_path}' does not exist.")

# else:
#     # Get all image file (common formats)
#     image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp")

#     try:
#         images = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]
#     except PermissionError:
#         print(f"Error: Permission denied to access '{folder_path}'. Try running as administrator.")
#     except Exception as e:
#         print(f"Error accessing folder: {e}")
#     else:
#         # Sort files alphabetically to maintain order
#         images.sort()

#         # Rename the first 20 images only
#         for index, filename in enumerate(images[:20], start=1):
#             ext = os.path.splitext(filename)[1] # Get the file extension
#             new_name = f"image{index}{ext}"
#             old_path = os.path.join(folder_path, filename )
#             new_path = os.path.join(folder_path, new_name)

#             try:
#                 os.rename(old_path, new_path)
#                 print(f"renamed: {filename} -> {new_name}")
#             except Exception as e:
#                 print(f"Error renaming {filename}: {e}")

# print("Renaming completed for 20 images!")

    