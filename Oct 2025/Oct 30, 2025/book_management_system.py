#
# Practice Question: Library Management System (CSV Based)
#
# Problem Statement:
# You are required to build a Library Management System using Python. The system will keep track of books available in the library and books
# issued by students. The data should be stored in CSV files, and the program should provide a menu-driven interface for the user.
#
# Requirements:
#
# 1. Store Data in CSV Files
# Use two CSV files:
# books.csv → Stores book details.
# issued_books.csv → Stores details of issued books.
#
# 2. Books Data Format (in books.csv)
# Each book record should be stored in the following format:
# book_id,title,author,available_copies
#
# Example:
# 101,Python Basics,John Smith,5
# 102,Data Science with Python,Jane Doe,2
#
# 3. Issued Books Data Format (in issued_books.csv)
# Each issued record should be stored in the following format:
# book_id,student_name,issue_date
#
# Example:
# 101,Ali,2025-08-27
# 102,Sara,2025-08-26
#
# 4. Menu Options
# The system should provide a menu like this:
# - Add a new book
# - View all books
# - Issue a book
# - View issued books
# - Return a book
# - Exit
#
# 5. Functional Requirements
#
# - Add a new book
# Ask user for book ID, title, author, and number of available copies.
# Store in books.csv.
#
# - View all books
# Display the contents of books.csv in a readable format.
#
# - Issue a book
# Ask for student name and book ID.
# If available copies > 0 → reduce by 1 and record issue in issued_books.csv with today’s date.
# Otherwise, show message: “Book not available.”
#
# - View issued books
# Read and display issued_books.csv.
#
# - Return a book
# Ask for book ID and student name.
#
# - Remove the record from issued_books.csv.
# Increase available copies in books.csv.

import csv


BOOKS_FILE_PATH = "books.csv"
ISSUED_BOOKS_FILE_PATH = "issued_books.csv"


# Read Books Function
def read_books(filepath):
    read_books_list = []
    with open(filepath, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            read_books_list.append(row)
    return read_books_list


# Write to File Function
def write_books(filepath, books):
    # Writes list of books to CSV file
    with open(filepath, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(books)


# Remove Books Function
def remove_books():
    """
    Removes a book from the system based on book ID.
    """
    book_id = get_book_id()
    search_results = search_book(book_id)

    if search_results:
        book_list = read_books(BOOKS_FILE_PATH)

        # Find and remove the book with matching ID
        for i, book in enumerate(book_list):
            if book[0].strip() == str(book_id):
                removed_book = book_list.pop(i)
                write_books(BOOKS_FILE_PATH, book_list)
                print(f"Book '{removed_book[1]}' (ID: {book_id}) successfully removed.")
                break
    else:
        print(f"Book with ID {book_id} not found in database. Please try again.")


def view_books():
    """
    Reads and displays all books from the CSV file in a formatted manner.
    """
    try:
        books = read_books(BOOKS_FILE_PATH)
        if len(books) > 0:
            # display header
            print()
            # Display each book record
            for row in books:
                if row:  # Skip empty rows
                    book_id = row[0] if len(row) > 0 else "N/A"
                    title = row[1] if len(row) > 1 else "N/A"
                    author = row[2] if len(row) > 2 else "N/A"
                    copies = row[3] if len(row) > 3 else "N/A"
                    print(f"{book_id:<10} {title:<30} {author:<25} {copies:<10}")
        else:
            # display some message like no books present
            print()

    except FileNotFoundError:
        print("Error: Book database file not found.")
    except Exception as e:
        print(f"Error reading books: {e}")


# Get Book ID Function
def get_book_id():
    while True:
        try:
            book_id_value = int(input("Enter book ID: "))
            break
        except:
            print("Invalid entry: must be integers")
    return book_id_value


# Search Book ID Function
def issue_books():
    """
    Issues a book to a user by decreasing the number of available copies by 1.
    Checks if the book exists and if copies are available before issuing.
    """
    book_id = get_book_id()
    search_results = search_book(book_id)

    if search_results:
        book_list = read_books(BOOKS_FILE_PATH)

        # Find the book and check availability
        for i, book in enumerate(book_list):
            if book[0].strip() == str(book_id):
                # Get current number of copies
                current_copies = int(book[3])

                if current_copies > 0:
                    # Issue the book - decrease copies by 1
                    book_list[i][3] = str(current_copies - 1)
                    write_books(BOOKS_FILE_PATH, book_list)

                    # Pending
                    # issued_books.csv update

                    print(f"\nBook issued successfully!")
                    print(f"Title: {book[1]}")
                    print(f"Author: {book[2]}")
                    print(f"Remaining copies: {book[3]}")
                else:
                    # Book is out of stock
                    print(f"\nSorry, '{book[1]}' is currently out of stock.")
                    print("Please check back later.")
                break
    else:
        print(f"Book with ID {book_id} not found in database. Please try again.")


# Add Books to CSV function
def add_books():
    """
    Ask user for book ID, title, author, and number of available copies.
    Validates all inputs before adding the book to the system.
    """
    # Get and validate book ID
    book_id = get_book_id()
    search_results = search_book(book_id)

    if search_results:
        print(f"Book {book_id} already exists. Please retry.")
    else:
        # Get and validate book title
        while True:
            title_input = input("Enter book title: ").strip()
            if title_input:
                break
            else:
                print("Title cannot be empty. Please enter a valid title.")

        # Get and validate author name
        while True:
            author_input = input("Enter author name: ").strip()
            if author_input:
                break
            else:
                print("Author name cannot be empty. Please enter a valid author.")

        # Get and validate number of copies
        while True:
            try:
                number_of_copies = int(input("Enter number of available copies: "))
                if number_of_copies > 0:
                    break
                else:
                    print("Number of copies must be greater than 0.")
            except ValueError:
                print("Invalid entry. Please enter a positive integer.")

        # Read existing books, add new book, and save
        list_of_books = read_books(BOOKS_FILE_PATH)
        list_of_books.append([str(book_id), title_input, author_input, str(number_of_copies)])
        write_books(BOOKS_FILE_PATH, list_of_books)

        print(f"Book '{title_input}' successfully added.")


# Issue Books Function
def issue_books():
    """
    Issues a book to a student by:
    1. Checking if book exists and has available copies
    2. Recording the issue in issued_books.csv
    3. Decreasing available copies in books.csv
    """
    from datetime import date

    # Get book ID from user
    book_id = get_book_id()

    # Read current books to check availability
    book_list = read_books(BOOKS_FILE_PATH)
    book_found = False
    book_available = False

    # Search for the book and check availability
    for i, book in enumerate(book_list):
        if book[0].strip() == str(book_id):
            book_found = True
            current_copies = int(book[3])

            if current_copies > 0:
                book_available = True

                # Get student name
                while True:
                    student_name = input("Enter student name: ").strip()
                    if student_name:
                        break
                    else:
                        print("Student name cannot be empty.")

                # Get today's date
                today = date.today().strftime("%Y-%m-%d")

                # Update books.csv - decrease copies
                book[3] = str(current_copies - 1)
                book_list[i] = book
                write_books(BOOKS_FILE_PATH, book_list)

                # Add to issued_books.csv
                issued_list = []
                try:
                    issued_list = read_books(ISSUED_BOOKS_FILE_PATH)
                except FileNotFoundError:
                    # If file doesn't exist, create empty list
                    pass

                issued_list.append([str(book_id), student_name, today])
                write_books(ISSUED_BOOKS_FILE_PATH, issued_list)

                print(f"\nBook issued successfully!")
                print(f"Title: {book[1]}")
                print(f"Student: {student_name}")
                print(f"Issue Date: {today}")
                print(f"Remaining copies: {book[3]}")
            else:
                print(f"\nSorry, '{book[1]}' is currently not available.")
                print("All copies are issued out.")
            break

    if not book_found:
        print(f"Book with ID {book_id} not found in database. Please try again.")


# Get User Input Function (Menu Choice)
def get_user_input_value():
    print("""\n1. Add Books  
2. View Books
3. Issue Books 
4. Update Books
5. Remove Books
6. Exit
""")
    check = 0
    while True:
        try:
            user_choice = int(input("Enter your choice: "))
            if user_choice > 0 or user_choice < 7:
                return user_choice
            else:
                print("Invalid entry. Please only enter numbers 1-6.")

        except:
            print("Invalid entry. Please only enter numbers 1-6.")


# Search Book Management System Function
def search_book(book_id):
    """
    Searches for a book by ID and returns True if found, False otherwise
    """
    try:
        book_list = read_books(BOOKS_FILE_PATH)
        for book in book_list:
            if book[0].strip() == str(book_id):
                return True
        return False
    except FileNotFoundError:
        return False


def update_books():
    """
    Updates book information (title, author, or number of copies).
    Allows user to modify existing book details.
    """
    book_id = get_book_id()

    # Read all books
    book_list = read_books(BOOKS_FILE_PATH)
    book_found = False

    # Search for the book
    for i, book in enumerate(book_list):
        if book[0].strip() == str(book_id):
            book_found = True

            # Display current book information
            print(f"\nCurrent Book Information:")
            print(f"Book ID: {book[0]}")
            print(f"Title: {book[1]}")
            print(f"Author: {book[2]}")
            print(f"Available Copies: {book[3]}")

            # Ask what to update
            print("\nWhat would you like to update?")
            print("1. Title")
            print("2. Author")
            print("3. Available Copies")
            print("4. Cancel")

            while True:
                try:
                    update_choice = int(input("Enter your choice: "))
                    if update_choice >= 1 and update_choice <= 4:
                        break
                    else:
                        print("Invalid entry. Please enter numbers 1-4.")
                except:
                    print("Invalid entry. Please enter numbers 1-4.")

            # Update based on choice
            if update_choice == 1:
                while True:
                    new_title = input("Enter new title: ").strip()
                    if new_title:
                        book[1] = new_title
                        print(f"Title updated successfully to '{new_title}'")
                        break
                    else:
                        print("Title cannot be empty.")

            elif update_choice == 2:
                while True:
                    new_author = input("Enter new author name: ").strip()
                    if new_author:
                        book[2] = new_author
                        print(f"Author updated successfully to '{new_author}'")
                        break
                    else:
                        print("Author name cannot be empty.")

            elif update_choice == 3:
                while True:
                    try:
                        new_copies = int(input("Enter new number of available copies: "))
                        if new_copies >= 0:
                            book[3] = str(new_copies)
                            print(f"Available copies updated successfully to {new_copies}")
                            break
                        else:
                            print("Number of copies cannot be negative.")
                    except ValueError:
                        print("Invalid entry. Please enter a valid number.")

            elif update_choice == 4:
                print("Update cancelled.")
                return

            # Save updated book list
            book_list[i] = book
            write_books(BOOKS_FILE_PATH, book_list)
            print("\nBook information updated successfully!")
            break

    if not book_found:
        print(f"Book with ID {book_id} not found in database. Please try again.")


# Main Function
def main():
    while True:
        user_choice = get_user_input_value()
        if user_choice == 6:
            print("You have successfully exited from the program")
            break
        if user_choice == 1:
            add_books()
        elif user_choice == 2:
            view_books()
        elif user_choice == 3:
            view_books()
            issue_books()
        elif user_choice == 4:
            update_books()
        else:
            remove_books()


main()
