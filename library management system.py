def library_system():
    library = {"Python": 3, "C++": 2, "Java": 4}
    
    while True:
        print("\nLibrary Menu")
        print("1. View Books\n2. Borrow Book\n3. Return Book\n4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Available books:", library)
        elif choice == 2:
            book = input("Enter book name to borrow: ")
            if book in library and library[book] > 0:
                library[book] -= 1
                print("You borrowed", book)
            else:
                print("Book not available")
        elif choice == 3:
            book = input("Enter book name to return: ")
            if book in library:
                library[book] += 1
                print("You returned", book)
            else:
                library[book] = 1
                print("New book added:", book)
        elif choice == 4:
            print("Exiting Library System")
            break
        else:
            print("Invalid choice")

library_system()
