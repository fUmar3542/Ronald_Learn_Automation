

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


#####################################################

# Practice Questions

# 1) Create a 2-dimensional list where each inner list contains
# the name of an item, its quantity, and its price. For example:

# inventory = [
#     ["Item A", 20, 15.5],
#     ["Item B", 35, 25.0]
# ]

# Use the append method to add a new item to the inventory.
# Use the insert method to insert the item after first item.
# Use a conditional statement to check if the total quantity of items
# in the inventory is greater than 100. Print "Inventory is sufficient" if true, otherwise print "Inventory is low."

# ------------------------------------------------------------

# 2) Create a 2-dimensional list where each inner list contains
# the day of the week and a list of events scheduled for that day. For example:

# schedule = [
#     ["Monday", ["Meeting", "Workshop"]],
#     ["Tuesday", ["Conference"]]
# ]

# Use the append method to add a new event to the list of events for Monday.
# Move an event to a different day (e.g., move the second event from Monday to Tuesday).
# Use a conditional statement to check if there are more than 3 events scheduled on any day. Print "Busy day"
# if true, otherwise print "Manageable day."


# ----------------------------------------------

# 3) Create a 2-dimensional list representing seats in a hall
# (e.g., 5 rows and 4 columns). Initialize all seats as "Available"

# Use the append method to add a new row of seats.
# Use the insert method to insert a new seat in a specific row (e.g., insert a new seat into the third row).
# Use a conditional statement to check if the first row is fully occupied.
# Print "Row is full" if true, otherwise print "Seats available."
