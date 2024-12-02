
# # Selection sort algorithm
# numbers_list = [32, 34, 5, 21, 78]
# if len(numbers_list) > 0:
#     for index in range(len(numbers_list)):
#         # Find the smallest number
#         smallest = index
#         for i in range(index, len(numbers_list)):
#             if numbers_list[i] < numbers_list[smallest]:
#                 smallest = i
#         # Swap
#         numbers_list[index], numbers_list[smallest] = numbers_list[smallest], numbers_list[index]
#     print(numbers_list)
# else:
#     print("Input list is empty.")


######################################################################################################################
# Problem Statement
# We have a list of strings. Write a program to sort the list items according to their length.

# Solution
# Find the smallest item length index in each iteration, then swap the items using smallest and iteration number index
#
# names_list = ['Umar', 'James', 'Bob', 'Ronald', 'Johnson', 'Paul', 'Ali']
#
# # Processing
# for index in range(len(names_list)):
#     smallest = index
#     for i in range(index, len(names_list)):
#         if len(names_list[i]) < len(names_list[smallest]):
#             smallest = i
#     names_list[index], names_list[smallest] = names_list[smallest], names_list[index]
#
# # output
# print(names_list)



##################################################################################
# Bubble Sort Algorithm

# Items of the list are like bubbles and we'll be doing swapping operation between
# these bubbles after checking their values

# numbers_list = [23, 12, 43, 17, 34, 9]
#
# for i in range(len(numbers_list)):
#     for j in range(len(numbers_list) - i - 1):
#         if numbers_list[j] > numbers_list[j+1]:
#             numbers_list[j], numbers_list[j+1] = numbers_list[j+1], numbers_list[j]
#
# print(numbers_list)


######################################################################################################################
# Problem Statement
# We have a list of strings. Write a program to sort the list items according to their length.

# Bubble Sort Algorithm

# names_list = ['Umar', 'James', 'Bob', 'Ronald', 'Johnson', 'Paul', 'Ali']
#
# for i in range(len(names_list)):
#     for j in range(len(names_list) - i - 1):
#         if len(names_list[j]) > len(names_list[j+1]):
#             names_list[j], names_list[j+1] = names_list[j+1], names_list[j]
#
# print(names_list)


###########################################################################
# Built-in functions


numbers_list = [23, 12, 43, 17, 34, 9]

numbers_list.sort()

# print(numbers_list)

names_list = ['Umar', 'james', 'Bob', 'Ronald', 'johnson', 'Paul', 'Ali']

names_list.sort()

# print(names_list)

# n = names_list.capitalize() # AttributeError: 'list' object has no attribute 'capitalize'

# For incase sensitive
names_list.sort(key=str.lower)

# print(names_list)


# Reverse the list

names_list.reverse()

print(names_list)


# Home Task

# Task 1
# ASCII - American standard Code for Information Integration

# Task 2
# Reverse the list with the help of indexing

