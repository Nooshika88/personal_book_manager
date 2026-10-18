from books import show_books, save_books, loads_book
from dotenv import load_dotenv
import os

load_dotenv()

name = input("enter your name : ")
print("wolcome ", name)


admin_mode = input("do you want to enter admin mode (yes/no)? ")
if admin_mode == "yes":
    admin_password = input("enter admin password: ")
    if admin_password == os.getenv("BOOK_MANAGER_ADMIN_PASSWORD"):
        print("admin mode activated")
    else:
        print("wrong password")

books = loads_book()
count = int(input("how many books do you want to add ? "))
for i in range(count):
    book = input("enter name of book : ")
    books.append(book)

show_books(books)
save_books(books)