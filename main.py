from books import show_books

name = input("enter your name : ")
print("wolcome ", name)
books = []
count = int(input("how many books do you want to add ? "))
for i in range(count):
    book = input("enter name of book : ")
    books.append(book)

show_books(books)