#docstring Question 8
"""This program implements a basic Library Management system using OOP.
It allows users to add, view, borrow, return, and search for books.
Book details are stored in a CSV file, and file handling along with exception
handling is used to manage data persistence."""

print(__doc__)
print()

import csv
class Book:
    def __init__(self,book_id,title,author,year,available = True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.available = available
class Library:
    def __init__(self):
        self.books = []
        self.load()
    
    def add(self):
        rng = int(input("Enter the no. of books you want to add: "))
        for i in range(rng):
            book_id = int(input("Enter the book id              : "))
            title =  input("Enter the title of the book    : ")
            author =  input("Enetr the author of the book   : ")
            year =  int(input("Enter the year of publication  : "))

            new_book = Book(book_id,title,author,year,True)
            self.books.append(new_book)
            self.save()
        print("New book(s) added successfully.")

    def load(self):
        try:
            with open("books.csv","r") as file:
                line = csv.reader(file)
                next(line)
                for l in line:
                    book_id = int(l[0])
                    title = l[1]
                    author = l[2]
                    year = int(l[3])
                    available = l[4] == "True"
                    self.books.append(Book(book_id,title,author,year,available))
        except FileNotFoundError:
            print("books.csv not found. ")
    def save(self):
        with open("books.csv","w", newline ="") as file:
            write = csv.writer(file)
            write.writerow(["Book ID","Title","Author","Year","Available"])
            for book in self.books:
                write.writerow([book.book_id, book.title, book.author, book.year, book.available])

    def borrow(self,book_id):
        for book in self.books:
            if book.book_id == book_id:
                    if book.available:
                        book.available = False
                        self.save()
                        print(f'{book.title} borrowed successfully.')
                    else:
                        print("Book already borrowed")
                    return
        print("Book not found.")
        
    def search(self,title):
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Book found : {book.title}")
                print(f"Author     : {book.author}")
                found = True
                break
        if not found:
            print(f"No books with the title {title} found.")
        
    def retrn(self,book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    self.save()
                    print(f'{book.title} returned successfully.')
                else:
                    print("Book already returned")
                return
        print("Book not found.")

    def show(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("\n----- List of Books -----\n")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f'ID      : {book.book_id}')
            print(f'Title   : {book.title}')
            print(f'Author  : {book.author}')
            print(f'Year    : {book.year}')
            print(f'Status  : {status}\n')
library = Library() 
while True:

    print("\n----- Library Management System -----\n")
    print("1. Add new books")
    print("2. View all books")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Search a book")
    print("6. Exit")

    ch = int(input("Select an action:"))

    if ch == 1:
        library.add()
    elif ch == 2:
        library.show()
    elif ch == 3:
        book_id = int(input("Enter book id to borrow : "))
        library.borrow(book_id)

    elif ch == 4:
        book_id = int(input("Enter book id to return : "))
        library.retrn(book_id)
    
    elif ch == 5:
        title = input("Enter book title to find: ")
        library.search(title)
    
    elif ch == 6:
        print("Thank you for trying this library management system.")
        break
    else:
        print("Invalid input!")