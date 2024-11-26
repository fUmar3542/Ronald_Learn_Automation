
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

numbers_list = [23, 12, 43, 23, 34, 9]

for i in range(len(numbers_list)):
    for j in range(len(numbers_list) - 1):
        if numbers_list[j] > numbers_list[j+1]:
            numbers_list[j], numbers_list[j+1] = numbers_list[j+1], numbers_list[j]

print(numbers_list)
