

# ************************************************

# List

# N-Dimensional lists

# one_dimentional = [1,2,3,4]                     # list
# print(one_dimentional[1])
#
# two_dimentional = [[1,2,3,4], [5,6,7,8]]        # lists in a list
# print(two_dimentional[1][2])
#
# three_dimentional = [
#                         [
#                             [1,2,3,4],
#                             [1,2,3,4],
#                             [5,6,7,8]
#                         ],
#                         [
#                             [1,2,3,4],
#                             [5,6,7,8]
#                         ]
#                     ]    # lists in lists in a list
# print(three_dimentional[0][1][0])
#
# # 1 2 3 4
# # 5 6 7 8
#
# country_list = [[[[], [[["name", "ssn", "phone"], ["name", "ssn", "phone"], ["name", "ssn", "phone"], ["name", "ssn", "phone"]], [], [], [], []]], [[]], [], []], [[]], [[], []] ]
#
#
# # x,y,z
#
# print(country_list)

# print(my_list[0])


###########################################################

# Access List Items

# integer_list = [1, 2, 3, 4, 5]
#
# print(integer_list[3])
#
# print(integer_list[1:4])
#
#
# # Change List Items
#
# age = 12
#
# integer_list[0] = 7
#
# age = 17
#
# print(integer_list)
#
# integer_list[1:4] = [7]
#
# print(integer_list)
#
#
# # [2, 3, 4] = [7, 8, 9]
# # [2, 3, 4] = [7]


# Add List Items

numbers = [1, 2, 3, 4]

numbers.append(5)

# print(numbers)
#
# temp1 = numbers[0:2]
# temp2 = numbers[2:]
#
# # [1,2] = [1,2]
# numbers = temp1
# numbers.append(5)
# numbers = numbers + temp2
#
# print(numbers)

numbers.insert(2, 5)

print(numbers)





# Remove List Items
# Loop Lists
# List Comprehension
# Sort Lists
# Copy Lists
# Join Lists
# List Methods
# List Exercises
