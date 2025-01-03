

# sum_of_columns = [sum(matrix[j][i] for j in range(number_of_columns)) for i in range(number_of_rows) for k in range(3)]


# Dictionary

# Hash tables
# Key value pairs


student1_dict = {
    "id": {"id1": 23},
    "email": "ronald.johnson@gmail.com",
    "name": ["Ronald Johnson", "Umar Farooq"],
}


# Access elements from the dictionary

# Keys
# print(student1_dict.keys())

# Values
# print(student1_dict.values())


# for id in student1_dict:
#     print(f"{id}: {student1_dict.get(id)}")

# items()

# for key, value in student1_dict.items():
#     print(f"{key}: {value}")


# Delete items from a dictionary

# 1st solution

# pop
# student1_dict.pop("email")
# print(student1_dict)


# 2nd solution

# popitem
# student1_dict.popitem()
# print(student1_dict)


# 3rd solution

# del

# del student1_dict["email"]
# print(student1_dict)
#
# del student1_dict
# print(student1_dict)


# 4th solution

# clear

# student1_dict.clear()
# print(student1_dict)

# a = 12


# Copy items from the dictionary

# 1st solution

student2_dict = {
    "id": {"id1": 24},
    "email": "ronald.johnson@gmail.com",
    "name": ["Ronald Johnson", "Umar Farooq"],
}

# student3_dict = student2_dict
# student2_dict['email'] = "ronald@gmail.com"

# student3_dict = student2_dict.copy()

# student3_dict = {}
# for key, value in student2_dict.items():
#     student3_dict[key] = value

# print(student3_dict)


# 2nd solution
# Constructor
#
# student3_dict = dict(student2_dict)
#
# print(student3_dict)


#################################################################################################################

#############################################################################################################

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




