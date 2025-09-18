# 📚 Library Management System (Python)

Author : M.S.MEYSINTHA

A Python-based project to manage books, users, and library operations.
This project simulates how a library works, with features like adding books, borrowing, returning, and displaying available books.
It is beginner-friendly and helps understand concepts of OOP (Object-Oriented Programming) in Python.

# 📌 Features

✅ Add Books – Add new books to the library’s collection
✅ Display Books – View all available books in the library
✅ Borrow Books – Issue books to users if available
✅ Return Books – Return borrowed books back to the library
✅ Looped Menu – User can perform multiple operations until they exit

# 📜 Code Example
class Library:
    def __init__(self, books):
        self.books = books

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(" -", book)

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"You have borrowed '{book_name}'. Please return it on time.")
        else:
            print("Sorry, this book is not available.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"Thank you for returning '{book_name}'.")


library = Library(["Python Basics", "Data Structures", "AI with Python", "Cyber Security"])

while True:
    print("\n=== Library Menu ===")
    print("1. Display Books\n2. Borrow Book\n3. Return Book\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        library.display_books()
    elif choice == 2:
        book = input("Enter book name to borrow: ")
        library.borrow_book(book)
    elif choice == 3:
        book = input("Enter book name to return: ")
        library.return_book(book)
    elif choice == 4:
        print("Thanks for using the Library Management System!")
        break
    else:
        print("Invalid choice. Try again.")

# ▶️ Example Run
=== Library Menu ===
1. Display Books
2. Borrow Book
3. Return Book
4. Exit
Enter choice: 1

Available Books:
 - Python Basics
 - Data Structures
 - AI with Python
 - Cyber Security

Enter choice: 2
Enter book name to borrow: Python Basics
You have borrowed 'Python Basics'. Please return it on time.

# ⚡ How to Run

Clone this repository:

git clone https://github.com/your-username/library-management-system.git
cd library-management-system


# Run the program:

python library.py

# output



# 🚀 Future Improvements

Add user accounts with login system

Track which user borrowed which book

Store data in text files or database (SQLite/MySQL)

Add fine system for late returns

Create a GUI version using Tkinter or PyQt
