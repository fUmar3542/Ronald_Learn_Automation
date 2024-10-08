
# String functions


# *******************************************************************

# Length

# first_name = "Umar"
#
# length = len(first_name)   # Argument passing to function
#
# print(length)

# *******************************************************************

# indexing

# 0   1  2
# a   b  c
# v1 v2 v3

# 0 -> a, 1 -> b, 2 -> c

# Index range -> 0 to (length of variable - 1)

first_name = "Umar"

# 0 1 2 3
# U m a r

# # Write a program to print the index range of the input given by User
#
# name = input("Enter you name: ")
# length = len(name)
#
# print("0 to "+ str(length-1))


# print(first_name[0])

length =  len(first_name)
end_index = length - 1

print(first_name[end_index])

print(first_name[len(first_name) - 1])


# *******************************************************************

# Practice Questions

# 1) Extract First, Last and Middle Characters:
#
# Given an input string from user, use indexing to extract the first, last and middle characters of the string. What are they?


# 2) Compare Lengths:
#
# Given two strings s1 = "Data" and s2 = "Science", compare their lengths and print which one is longer.


# 3) Check Empty String:
#
# Write a Python function that checks if a given string is empty or not by evaluating its length.
