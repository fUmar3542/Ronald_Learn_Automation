
#####################################################
# Task
# Reverse the list with the help of indexing/operator

# Task 1
# Do it with the for loop

# name = "Umar Farooq"
# reverse_list = []
# length = len(name)
#
# for i in range(length):
#     index = length - i - 1
#     reverse_list.append(name[index])
#
# print(''.join(reverse_list))


# Task 2
# Do it in a single line

# print(name[::-1])


###########################################
# Sort

# names_list = ['Umar', 'james', 'Bob', 'Ronald', 'johnson', 'Paul', 'Ali']

# names_list.sort(key=str.lower)

# Ascending
# names_list.sort()

# print(names_list)

# Descending
# names_list.sort(key=str.lower)
#
# names_list.reverse()
#
# print(names_list)


# Descending

# names_list.sort(key=str.lower, reverse=True)
#
# # names_list.sort(key=myfunc)
#
# print(names_list)


######################################################
# Copying of lists

names_list = ['Umar', 'james', 'Bob', 'Ronald', 'johnson', 'Paul', 'Ali']

# names_list -> address -> ['Umar', 'james', 'Bob', 'Ronald', 'johnson', 'Paul', 'Ali']

# Can't do this operation
# second_list = names_list

# # Solution 1 - Built-in function
# second_list = names_list.copy()
#
# names_list[0] = "Sam"
#
# print(second_list)
# print(names_list)


# Solution 2
# second_list = []
# for item in names_list:
#     second_list.append(item)
#
# print(second_list)


# Solution 3
# second_list = names_list[:]
#
# print(second_list)


# Datatype conversion
# number = int("123")


# Solution 4
second_list = list(names_list)

names_list[0] = "Sam"
#
# print(second_list)


################################################
# Joining of lists

# Solution 1
# third_list = []
# for item in names_list:
#     third_list.append(item)
# for item in second_list:
#     third_list.append(item)
#
# print(third_list)


# Solution 2
# third_list = names_list + second_list
#
# print(third_list)


# Solution 3
# third_list = names_list.copy()
# third_list += second_list.copy()
# print(third_list)


# Solution 4
third_list = []
third_list.extend(names_list)
third_list.extend(second_list)
print(third_list)




