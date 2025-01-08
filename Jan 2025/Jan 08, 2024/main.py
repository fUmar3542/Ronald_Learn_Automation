
# 1) Library Management System
# Simulate a simple library system that:
#
# Maintains a dictionary of books where the keys are book titles and values are the number of copies available.
#
# Allows users to:
# - Borrow a book (reduce the available count by 1).
# - Return a book (increase the available count by 1).
# - Check the availability of a specific book.
# - Stops the program when the user enters "exit."
#
# Bonus: Prevent borrowing if a book is out of stock.
#
# ####################################################
# # Examples
# ####################################################
#
# ****************************************************
#
# # Input
#
# Library System Options:
# 1. Borrow a book
# 2. Return a book
# 3. Check book availability
# 4. Exit
#
# Enter your choice: 1
# Enter the name of the book you want to borrow: The Great Gatsby
#
#
# # Output
# You have successfully borrowed 'any book name'.
#
# ****************************************************
#
# # Input
#
# Library System Options:
# 1. Borrow a book
# 2. Return a book
# 3. Check book availability
# 4. Exit
#
# Enter your choice: 3
# Enter the name of the book to check availability: 1984
#
# # Output
#
# '1984' is available. Copies left: 5.
#
#
# ****************************************************
#
# # Input
#
# Library System Options:
# 1. Borrow a book
# 2. Return a book
# 3. Check book availability
# 4. Exit
#
# Enter your choice: 1
# Enter the name of the book you want to borrow: Pride and Prejudice
#
#
# # Output
#
# Sorry, 'Pride and Prejudice' is out of stock.

#############################################################################################################

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

# # Customer side
#
# # Input
# while True:
#     try:
#         user_choice = int(input("Library System Options:\n 1. Borrow a book\n 2. Return a book\n 3. Check book availability\n 4. Exit \n\n Enter your choice: "))
#         if user_choice not in [1,2,3]:
#             user_input_2 = input(f"Please enter the book name: ").lower()
#             if user_input_2 in book_list:
#                 if user_choice == 1:
#                     if book_list[user_input_2] > 0:
#                         book_list[user_input_2] = book_list[user_input_2] - 1
#                         print(f"You have successfully borrowed {user_input_2}.")
#                         print("Please return within 30 business days.\n")
#                 elif user_choice == 2:
#                     book_list[user_input_2] = book_list[user_input_2] + 1
#                     print(f"Thank you for returning {user_input_2}.")
#                 elif user_choice == 3:
#                     if book_list[user_input_2] > 0:
#                         print(f"{user_input_2} is available. Copies left: {book_list[user_input_2]}")
#                     else:
#                         print(f"Sorry, {user_input_2} is out of stock")
#             else:
#                 print(f"Error: {user_input_2} is not in our inventory system. Please try again.")
#         elif user_choice == 4:
#             print("Thank you for your patronage. Have a good day!")
#             break
#         else:
#             print("Invalid choice\n")
#     except:
#         print("\nError: please enter a valid number\n")


# Admin side

# CRUD -> Create, Read, Update, Delete

# Create -> Add books
# Read -> Display the books in a proper format
# Update -> The admin can update the quantities or the name of he books
# Delete -> The admin can delete the specific book from the database





# # Variables
# check = False
# user_choice = 0
# choice_1 = "enter the book that you would like to borrow"
# choice_2 = "enter the book that you would like to return"
# choice_3 = "enter the book that you would like to check availability for"
# book_list = {"1984": 5,
#              "to kill a mockingbird": 5,
#              "sapiens": 5,
#              "pride and prejudice": 5,
#              "the great gatsby": 5,
#              "Bible": 5,
#              "dune": 5,
#              "lord of the rings": 5,
#              "in the vineyard of the text": 5,
#              "amusing ourselves to death": 5}
#
# # Input
# while True:
#     try:
#         user_input = int(input("Library System Options:\n 1. Borrow a book\n 2. Return a book\n 3. Check book availability\n 4. Exit \n\n Enter your choice: "))
#         user_choice = user_input
#         if user_choice == 1:
#             user_input_2 = input(f"Please {choice_1}: ")
#             if user_input_2 in book_list:
#                 book_list[f"{user_input_2}"] = book_list[f"{user_input_2}"] - 1
#                 if book_list[f"{user_input_2}"] > 0:
#                     print(f"You have successfully borrowed {user_input_2}.")
#                     print("Please return within 30 business days.")
#                     print("")
#                 else:
#                     print(f"Sorry, {user_input_2} is out of stock")
#                     print("")
#             if user_input_2 not in book_list:
#                 print(f"Error: {user_input_2} is not in our inventory system. Please try again.")
#         elif user_choice == 2:
#             user_input_2 = input(f"Please {choice_2}: ")
#             if user_input_2 in book_list:
#                 book_list[f"{user_input}"] = book_list[f"{user_input_2}"] + 1
#                 print(f"Thank you for returning {user_input_2}.")
#             else:
#                 print("Error: Invalid bar code. Please see admin")
#         elif user_choice == 3:
#             user_input_2 = input(f"Please {choice_3}: ")
#             if book_list[f"{user_input_2}"] > 0:
#                 print(f"{user_input_2} is available. Copies left: {book_list[user_input_2]}")
#             else:
#                 print(f"Sorry, {user_input_2} is out of stock")
#         else:
#             print("Thank you for your patronage. Have a good day!")
#             break
#     except:
#         print("")
#         print("Error: please enter a valid number\n")
