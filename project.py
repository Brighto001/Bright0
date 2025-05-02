# import calendar
# #Igbo market days
# market_days = ["Eke", "Orie", "Afor", "Nkwo"]

# def print_igbo_calender(year):
#     print(f"Igbo Calender for the Year {year}\n")

#     for month in range(1, 13): # Loop through all 12 months
#         print(f"{calendar.month_name[month]} {year}".center(30, "_"))
#         print("Sun Mon Tue Wed Thu Fri Sat Market Day translation")

#         #Get the first weekday and total days in the month
#         first_weekday, num_days = calendar.monthrange(year, month)

#         week = ["       "] * first_weekday # offset for the first week
#         market_day_counter = first_weekday # Align market days

#         for day in range(1, market_day + 1):
#             market_day = (market_day_counter)  
#             week.append(f"{day:2} {market_day[:3]} ")
#             market_day_counter += 1

        
#     if len(week) ==7: # End of a weeek
#         print("  ".join(week))
#         week = []

#     # Print remaining days
#         if week: 
#             print("  ".join(week))

#             print("\n" + "_" * 40)

# # user input
# year = int(input("Enter the year: "))
# language = input("Enter your preferred language(Default: English): ")

class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []
    
    def add_book(self, title, author):
        new_book = self.Book(title, author)
        self.books.append(new_book)
 
    def list_books(self):
        print(f"Books in {self.library_name}:")
        for book in self.books:
            print(book.get_info())

# Inner class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}"
    
# Usage
library = Library("Central Library")
library.add_book("1984", "George Orwell")
library.add_book("To kill a Mockingbird", "Harper Lee")

library.list_books()