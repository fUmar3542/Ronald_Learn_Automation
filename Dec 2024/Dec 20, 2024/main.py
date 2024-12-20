
###################################################
# Intersection

# set1 = {1,2,4,3}
# set2 = {4,5,3}
# set3 = {45, 43}

# 1)
# set1 = set1.intersection(set2, set3)
#
# print(set1)

# 2)
# set1 = set1 & set2 & set3
# print(set1)

# 3)

# set1.intersection_update(set2)
#
# print(set1)



###################################################
list1 = [1, 2, 4, 67, 54]
list2 = [4, 5, 3]

# Approach

# 1) Go through all elements of first list, one by one
# 2)    if the value is present in the list2
# 3)        append it to the resultant list


# Key search operation
# O(n*n)

# Cost of the operations

# n -> length of list

# O(n/2)
# O(1)


#################################################

# Difference between 2 sets

set1 = {1,2,3,4}
set2 = {4,5,3}
set3 = {45, 43}

# 1)
# set1 = set1.difference(set2)
#
# print(set1)

# 2)
# set1.difference_update(set2)
#
# print(set1)


# 3)

# set1 = set1 - set2
# print(set1)


#######################################################

# Symmetric Difference

# The resultant set will be containing all the elements from
# set 1 and set 2 which are not common between these 2 sets

# 1)
# set1 = set1.symmetric_difference(set2)
# print(set1)

# 2)
# set1.symmetric_difference_update(set2)
# print(set1)

# 3)
# set1 = set1 ^ set2
# print(set1)


#########################################################
# Home Work

# Write a code in order to perform the difference and
# symmetric difference between 2 lists

