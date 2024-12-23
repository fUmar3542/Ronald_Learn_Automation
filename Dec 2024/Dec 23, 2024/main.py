
# set1 = {1,2,3}
# set2 = {3,4,5}

# set1 = set1.difference(set2)
#
# print(set1)

# set1.difference_update(set2)
#
# print(set1)


# set1.symmetric_difference_update(set2)
#
# print(set1)



#############################################################

# Difference
set_1 = [1,2,3,4,5,6]
set_2 = [1,2,7,8,9,10]
difference_list = []
difference_list_2 = []

# for i in set_1:
#     if i not in set_2:
#         difference_list.append(i)

# Symmetric Difference
for i in set_1:
    if i not in set_2:
        difference_list.append(i)

for j in set_2:
    if j not in set_1:
        difference_list_2.append(j)

# print(difference_list)
# print(difference_list_2)

set_1 = difference_list
print(set_1)

set_1 = difference_list + difference_list_2
print(set_1)





###############################################################
# Practice Questions

# Set Operations on Lists
#
# Write a program to perform the following tasks:
#
# 1) Take two lists of integers from the user.
# 2) Convert them into sets and find:
# 3) Union of the two sets
# 4) Intersection of the two sets
# 5) Difference (elements in the first set but not in the second)
#
#
# Input:
#
# Enter the first list of integers: 1 2 3 4 5
# Enter the second list of integers: 4 5 6 7 8
#
# Output:
#
# Union: {1, 2, 3, 4, 5, 6, 7, 8}
# Intersection: {4, 5}
# Difference: {1, 2, 3}
#
#
# ------------------------------------------------------------------------
#
# Matrix Manipulation
#
# Write a Python program to:
#
# 1) Accept a 3x3 matrix (list of lists) from the user.
# 2) Find the sum of each row and sum of each column.
# 3) Print the matrix, row sums, and column sums.
#
# Input:
#
# Enter elements of the 3x3 matrix row by row:
# 1 2 3
# 4 5 6
# 7 8 9
#
#
# Output:
#
# Matrix:
# 1 2 3
# 4 5 6
# 7 8 9
#
# Row Sums: [6, 15, 24]
# Column Sums: [12, 15, 18]








