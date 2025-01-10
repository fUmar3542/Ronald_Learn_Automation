
# Task: Menu for the user and an admin


# Variables
user_choice = 0
book_list = {"1984": 5,
             "to kill a mockingbird": 5,
             "sapiens": 5,
             "pride and prejudice": 5,
             "the great gatsby": 5,
             "Bible": 5,
             "dune": 5,
             "lord of the rings": 5,
             "in the vineyard of the text": 5,
             "amusing ourselves to death": 0}

# Customer side

# Input
while True:
    try:
        user_choice = int(input("Library System Options:\n 1. Borrow a book\n 2. Return a book\n 3. Check book availability\n 4. Exit \n\n Enter your choice: "))
        if user_choice in [1, 2, 3]:
            user_input_2 = input(f"Please enter the book name: ").lower()
            if user_input_2 in book_list:
                if user_choice == 1:
                    if book_list[user_input_2] > 0:
                        book_list[user_input_2] = book_list[user_input_2] - 1
                        print(f"You have successfully borrowed {user_input_2}.")
                        print("Please return within 30 business days.\n")
                elif user_choice == 2:
                    book_list[user_input_2] = book_list[user_input_2] + 1
                    print(f"Thank you for returning {user_input_2}.")
                elif user_choice == 3:
                    if book_list[user_input_2] > 0:
                        print(f"{user_input_2} is available. Copies left: {book_list[user_input_2]}")
                    else:
                        print(f"Sorry, {user_input_2} is out of stock")
            else:
                print(f"Error: {user_input_2} is not in our inventory system. Please try again.")
        elif user_choice == 4:
            print("Thank you for your patronage. Have a good day!")
            break
        else:
            print("Invalid choice\n")
    except:
        print("\nError: please enter a valid number\n")


# Admin side

# CRUD -> Create, Read, Update, Delete
while True:
    try:
        admin_choice = int(input("\nAdmin System Options:\n 1. Add Book \n 2. Display Inventory \n 3. Update Inventory \n 4. Delete Book \n 5. Exit \n\n Enter your choice: "))
        if admin_choice == 5:
            print("You have successfully exited the admin system.")
            break
        if admin_choice in [1,2,3,4]:
            if admin_choice == 1:
                book_to_add = input("Enter book to add: ").lower()
                # get quantity from the user
                book_list[book_to_add] = 1
            elif admin_choice == 2:
                # Display the items in a proper format
                print(book_list)
            elif admin_choice == 3:
                while True:
                    book_to_update_choice = int(input("\nUpdate Inventory Options:\n 1. Update Book Title \n 2. Update Stock Count \n 3. Return to Main Menu.\n\n Enter your choice: "))
                    if book_to_update_choice in [1,2,3]:
                        if book_to_update_choice == 1:
                            update_title_choice = input("Enter book title to update: ").lower()
                            if update_title_choice in book_list:
                                modify_title_to = input("Enter new book title: ").lower()
                                if modify_title_to not in book_list:
                                    book_list[modify_title_to] = book_list.pop(update_title_choice)
                                    print(f"{update_title_choice} successfully changed to {modify_title_to}\n\n")
                                else:
                                    print(f"Sorry, {modify_title_to} is already present in our database")
                            else:
                                print(f"Sorry, {update_title_choice} is not available in the inventory.")
                        elif book_to_update_choice == 2:
                            book_to_update_stock_count = input("Enter book title to update stock count: ").lower()
                            if book_to_update_stock_count in book_list:
                                modify_count_to = int(input("Enter new stock count: "))
                                if modify_count_to > 0:
                                    book_list[book_to_update_stock_count] = modify_count_to
                                    print(f"Stock count for '{book_to_update_stock_count}' updated to {modify_count_to}.")
                                else:
                                    print("Invalid entry: must be a positive integer")
                            else:
                                print(f"Sorry, {book_to_update_stock_count} is not available in the inventory.")
                        elif book_to_update_choice == 3:
                            print("You have successfully exited the update inventory menu.\n")
                            break
                    else:
                        print(f"Error: invalid entry. {book_to_update_choice} not available as an option.")
            elif admin_choice == 4:
                delete_book_choice = input("Enter book to delete: ").lower()
                if delete_book_choice in book_list:
                    book_list.pop(delete_book_choice)
                    print(f"{delete_book_choice} has been successfully deleted from the inventory.")
                else:
                    print(f"Sorry, {delete_book_choice} is not available.")
        else:
            print(f"Error: invalid entry. {admin_choice} not available as an option.")
    except:
        print("Error: selected option is not available.\n")
