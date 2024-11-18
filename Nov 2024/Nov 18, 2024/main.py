#####################################################################################
# Quiz Question
#####################################################################################
# Write a program to create new list of names in upper case format from the old list.

old_names = ['ronald', 'umar', 'james']
# new_list = []
#
# # for i in range(len(old_names)):
# #     upper_case_name = old_names[i].upper()
# #     new_list.append(upper_case_name)
#
# for name in old_names:
#     upper_case_name = name.upper()
#     new_list.append(upper_case_name)


# # For loop
#
# # For range loop
# for i in range(5):
#     print(i)
#
# # For each loop
# for item in some_list:
#     print(item)


#############################
# List Comprehension

# list_name = [expression for item in some_list]

# expression is either the same value or the resultant value which we have to store in the resultant list

# 1) for loop iterations
# 2) expression evaluation
# 3) appending of elemnts

new_list = [name.upper() for name in old_names]

new_list = [old_names[i].upper() for i in range(len(old_names))]



