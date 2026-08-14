class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display_book(self):
        status = "Available" if self.is_available else "Issued"

        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("----------------------------")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists!")
                return

        new_book = Book(book_id, title, author)
        self.books.append(new_book)

        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
            return

        print("\n----- Library Books -----")

        for book in self.books:
            book.display_book()

    def search_book(self):
        search = input("Enter Book ID or Title: ")

        found = False

        for book in self.books:
            if (book.book_id == search or
                    book.title.lower() == search.lower()):

                book.display_book()
                found = True

        if not found:
            print("Book not found.")

    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")

        for book in self.books:
            if book.book_id == book_id:

                if book.is_available:
                    book.is_available = False
                    print("Book issued successfully!")
                else:
                    print("This book is already issued.")

                return

        print("Book not found.")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        for book in self.books:
            if book.book_id == book_id:

                if not book.is_available:
                    book.is_available = True
                    print("Book returned successfully!")
                else:
                    print("This book was not issued.")

                return

        print("Book not found.")


library = Library()


while True:

    print("\n----- Library Management System -----")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please enter 1-6.")