

# Set

# Advantages
# 1) Values without duplicates
# 2) In order to add/remove elements, it provides us the optimized way b/c of hash tables
# 3) Operations

# Operations

##############################################
# Union

# list1 = [1,2,3,4]
# list2 = [4,5,3]

# [5] + list1 -> [1,2,3,4,5]

# largest_list = list2
# smallest_list = list1
# if len(list1) > len(list2):
#     largest_list = list1
#     smallest_list = list2
#
# for i in smallest_list:
#     if i not in largest_list:
#         largest_list.append(i)
#
# list1 = largest_list
# print(list1)

########################################
# For loops

# list1 = [1,2,3,4]
#
# for i in list1:
#     print(i)
#
# for i in range(len(list1)):
#     print(list1[i])
########################################

# {1,2,3,4} union {4,5,3} -> {1,2,3,4,5}

set1 = {1,2,3,4}
set2 = {4,5,3}
set3 = {45, 43}

# 1)

# set1.update(set2)
#
# print(set1)

# 2)

# set1 = set1.union(set2, set3)  # n number of arguments
#
# print(set1)

# 3)

# set1 = set1 | set2 | set3
#
# print(set1)


###################################################
# Intersection

# 1)
# set1 = set1.intersection(set2, set3)
#
# print(set1)

# 2)
set1 = set1 & set2 & set3

print(set1)


list1 = [1,2,3,4]
list2 = [4,5,3]

# Approach


