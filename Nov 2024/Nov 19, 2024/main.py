

###################################################################
# List Comprehension

# list_name = [expression for item in some_list]

# expression is either the same value or the resultant value which we have to store in the resultant list

# 1) for loop iterations
# 2) expression evaluation
# 3) appending of elemnts

###############################################################################
# Problem Statement: Only convert it to upper case if its length is less than 6

# old_names = ['ronald', 'umar', 'james']
# new_list = []
#
# # for name in old_names:
# #     if len(name) < 6:
# #         upper_case_name = name.upper()
# #         new_list.append(upper_case_name)
#
# new_list = [name.upper() for name in old_names if len(name) < 6]
#
# print(new_list)


################################################################
# Sorting of lists

# numbers_list = [32, 34, 5, 21, 78]
# resultant_list = []

# Initiate a For loop to go through all the elements one by one
#   Use a for loop to find the smallest number
#   if numbers_list[index] < numbers_list[index+1]:
#

numbers_list = [32, 34, 5, 21, 78]
# We have to find and print the smallest number in the list

smallest = -1
for i in range(0, len(numbers_list)):
    for j in range(len(numbers_list)):
        if numbers_list[i] < numbers_list[j]:
            smallest = numbers_list[i]

print(smallest)


# Solution 2

